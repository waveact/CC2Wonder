import bpy, os, json, string

class CC2WonderAction(bpy.types.Operator):
    bl_idname = "object.cc2wonder_action"
    bl_label = "Save"
    
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    
    def execute(self, context):
        addon_path = os.path.dirname(os.path.realpath(__file__))
        resource_path = os.path.join(addon_path, "resource")
        expression_data_path = os.path.join(resource_path, "expression.json")
        bone_data_path = os.path.join(resource_path, "bone.json")

        with open(expression_data_path,'r') as f: 
            self.expression_data = json.load(f) 

        with open(bone_data_path,'r') as f: 
            self.bone_data = json.load(f) 
        
        self.generated_strings = []
        
        armature_name = "Armature"
        armature = bpy.data.objects.get(armature_name)
        armature.name = "CC_BODY"
        
        self.armature = armature
        
        self.mesh_name = "CCMesh"
        
        self.udim = {"1001":"Head", "1002":"Body", "1003":"Arm", "1004":"Leg", "1005":"Nail", "1006":"Eyalash"}
        
        filepath = bpy.path.abspath(self.filepath)
        self.folder_path = os.path.dirname(filepath)
   
        self.shape_key_mesh = None
        
        self.mesh_obj_list = []
        
        occlusion_obj = bpy.data.objects.get("CC_Base_EyeOcclusion")
        if occlusion_obj is not None:
            bpy.data.objects.remove(occlusion_obj, do_unlink=True)
        
        tearline_obj = bpy.data.objects.get("CC_Base_TearLine")
        if tearline_obj is not None:
            bpy.data.objects.remove(tearline_obj, do_unlink=True)
        
        for obj in bpy.data.objects:
            if obj.parent == self.armature and obj.type == "MESH":
                #obj.name = self.mesh_name + "_FACE"
                self.mesh_obj_list.append(obj)
        
        self.delete_all_shape_key_actions()
        self.delete_bone_animations()
        
        self.reset_shape_keys()
        
        self.rename_bones()
        self.change_bone_parent()
        
        self.rename_mesh()
        
        self.build_material()
        
        self.merge_shape_keys("Eye_L_Look_L", "Eye_R_Look_L", "eyeL")
        self.merge_shape_keys("A10_Eye_Look_Out_Left", "A12_Eye_Look_In_Right", "eyeL")
        
        self.merge_shape_keys("Eye_L_Look_R", "Eye_R_Look_R", "eyeR")
        self.merge_shape_keys("A11_Eye_Look_In_Left", "A13_Eye_Look_Out_Right", "eyeR")
        
        self.merge_shape_keys("Eye_L_Look_Up", "Eye_R_Look_Up", "eyeUp")
        self.merge_shape_keys("A06_Eye_Look_Up_Left", "A07_Eye_Look_Up_Right", "eyeUp")
        
        self.merge_shape_keys("Eye_L_Look_Down", "Eye_R_Look_Down", "eyeDn")
        self.merge_shape_keys("A08_Eye_Look_Down_Left", "A09_Eye_Look_Down_Right", "eyeDn")
        
        self.merge_shape_keys("Mouth_Roll_Out_Lower_L", "Mouth_Roll_Out_Lower_R", "lipPoutLower")
        self.merge_shape_keys("Mouth_Roll_Out_Upper_L", "Mouth_Roll_Out_Upper_R", "lipPoutUpper")
        self.merge_shape_keys("Mouth_Push_Lower_L", "Mouth_Push_Lower_R", "lipPushLower")
        self.merge_shape_keys("Mouth_Push_Upper_L", "Mouth_Push_Upper_R", "lipPushUpper")
        self.merge_shape_keys("Mouth_Roll_In_Lower_L", "Mouth_Roll_In_Lower_R", "lipSuckLower")
        self.merge_shape_keys("Mouth_Roll_In_Upper_L", "Mouth_Roll_In_Upper_R", "lipSuckUpper")
        self.merge_shape_keys("Nose_Nostril_In_L", "Nose_Nostril_In_R", "noseCompress")
        self.merge_shape_keys("Nose_Nostril_Dilate_L", "Nose_Nostril_Dilate_R", "noseFlare")
        self.merge_shape_keys("Mouth_Funnel_Down_L", "Mouth_Funnel_Down_R", "lipFunnelerLower")
        self.merge_shape_keys("Mouth_Funnel_Up_R", "Mouth_Funnel_Up_L", "lipFunnelerUpper")
        self.merge_shape_keys("Mouth_Pucker_Up_L", "Mouth_Pucker_Up_R", "lipPucker_Up")
        self.merge_shape_keys("Mouth_Pucker_Down_L", "Mouth_Pucker_Down_R", "lipPucker_Dn")
        self.merge_shape_keys("lipPucker_Up", "lipPucker_Dn", "lipPucker")
        self.merge_shape_keys("Mouth_Smile_L", "Mouth_Down_Lower_L", "lipSmileOpenL")
        self.merge_shape_keys("Mouth_Smile_R", "Mouth_Down_Lower_R", "lipSmileOpenR")
        self.merge_shape_keys("Mouth_Pull_Upper_R", "Mouth_Up_Upper_R", "lipSneerR")
        self.merge_shape_keys("Mouth_Pull_Upper_L", "Mouth_Up_Upper_L", "lipSneerL")
        
        self.create_stick_shape_keys()
        
        self.rename_shape_keys()
        
        self.assign_driver()
        
        self.connect_shape_keys()
        
        #self.reset_shape_keys()
        
        self.create_collection_and_move_armature()
        
        if not filepath.lower().endswith(".blend"):
            filepath += ".blend"

        bpy.ops.wm.save_as_mainfile(filepath=filepath)
        
        self.report({'INFO'}, "Export CC Character to Wonder")
        
        return {'FINISHED'}
  
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    def process_string(self, _input_string):
        cleaned_string = ''.join(c for c in _input_string if c.isalpha())
        
        if cleaned_string == "":
            while True:
                random_string = ''.join(random.sample(string.ascii_lowercase, 7))
                if random_string not in self.generated_strings:
                    self.generated_strings.append(random_string)
                    return random_string
        else:
            return cleaned_string

    def delete_all_shape_key_actions(self):
        for a in bpy.data.actions:
            bpy.data.actions.remove(a)
            
    def delete_bone_animations(self):
        if self.armature.data.animation_data and self.armature.data.animation_data.action:
            bpy.data.actions.remove(self.armature.data.animation_data.action)
        
        bone_list = ["CC_Base_NeckTwist02", "CC_Base_FacialBone", "CC_Base_JawRoot", "CC_Base_R_Eye", "CC_Base_L_Eye", "CC_Base_UpperJaw", "CC_Base_Teeth01", "CC_Base_Tongue01", "CC_Base_Tongue02", "CC_Base_Tongue03", "CC_Base_Teeth02"]
        
        for i in range(len(bone_list)):
            name = bone_list[i]
            pb = self.armature.pose.bones.get(name) # None if no bone named name
            pb.location = (0, 0, 0)
            pb.rotation_quaternion =(1.0, 0.0, 0.0, 0.0)
        
        
    def rename_bones(self):
        bpy.ops.object.mode_set(mode='POSE')
    
        for name in self.bone_data:
            # get the pose bone with name
            bone = self.armature.pose.bones.get(name)
            # continue if no bone of that name
            if bone is None:
                continue
            # rename
            bone.name = self.bone_data[name]
            
        bpy.ops.object.mode_set(mode='OBJECT')
    
    def rename_mesh(self):
        
        self.generated_strings = []
        if len(self.mesh_obj_list) == 1:
            self.mesh_obj_list[0].name = self.mesh_name + "_FACE"
            self.mesh_obj_list[0].data.name = self.mesh_name
            self.shape_key_mesh = self.mesh_obj_list[0]
        
        for i in range(len(self.mesh_obj_list)):
            if self.mesh_obj_list[i].name == "CC_Base_Body":
                self.mesh_obj_list[i].name = self.mesh_name + "_Base_FACE"
                self.mesh_obj_list[i].data.name = self.mesh_name + "_Base"
                self.shape_key_mesh = self.mesh_obj_list[i]
                
            elif self.mesh_obj_list[i].name == "CC_Game_Body":
                self.mesh_obj_list[i].name = self.mesh_name + "_Base_FACE"
                self.mesh_obj_list[i].data.name = self.mesh_name + "_Base"
                self.shape_key_mesh = self.mesh_obj_list[i]
            else:    
                new_name = self.process_string(self.mesh_obj_list[i].name)
                self.mesh_obj_list[i].name = new_name
                self.mesh_obj_list[i].data.name = new_name
            
    
    def build_material(self):
        folder_path = self.folder_path
        
        for i in range(len(self.mesh_obj_list)):
            mesh_obj = self.mesh_obj_list[i]
            mesh_name = self.mesh_obj_list[i].data.name
            materials = mesh_obj.data.materials
    
            if (len(materials) > 1) and (mesh_name != self.mesh_name + "_Base"):
                for poly in mesh_obj.data.polygons:
                    material_index = poly.material_index
                    if material_index < len(materials):
                        for loop_index in poly.loop_indices:
                            uv_layer = mesh_obj.data.uv_layers.active.data[loop_index]
                            uv = uv_layer.uv
        
                            uv[0] += material_index
                            uv[1] += 0
            
            diffuse_texture_set = []
            normal_texture_set = []
            opacity_texture_set = []
            
            for j in range(len(materials)):
                material = materials[j]
            
                udim_index = 1001 + j
                
                nodes = material.node_tree.nodes
                
                bsdf = None
                
                diffuse_channel = None
                normal_channel = None
                opacity_channel = None
                
                for node in nodes:
                    if node.type == "BSDF_PRINCIPLED":
                        bsdf = node
                        if len(bsdf.inputs["Base Color"].links) > 0:
                            diffuse_channel = bsdf.inputs["Base Color"].links[0].from_node
                            
                        if len(bsdf.inputs["Normal"].links) > 0:
                            normal_channel = bsdf.inputs["Normal"].links[0].from_node
                            
                        if normal_channel.type == 'NORMAL_MAP':
                            if len(normal_channel.inputs["Color"].links) > 0 :
                                normal_channel = bsdf.inputs["Normal"].links[0].from_node.inputs["Color"].links[0].from_node
        
                for node_image in nodes:
                    if node_image.type == 'TEX_IMAGE':
                        if (node_image == diffuse_channel):
                            texture_path = bpy.path.abspath(node_image.image.filepath)
                            node_image.image.name = mesh_name + "_" + str(udim_index) + "_TEX_DIFF"
                            output_path = (folder_path + "\\" + node_image.image.name+".png")
                            node_image.image.save_render(output_path)
                            
                            diffuse_texture_set.append(output_path)
        
                for node_image in nodes:
                    if node_image.type == 'TEX_IMAGE':
                        if (node_image == normal_channel):
                            texture_path = bpy.path.abspath(node_image.image.filepath)
                            node_image.image.name = mesh_name + "_" + str(udim_index) + "_TEX_NORM"
                            output_path = (folder_path + "\\" + node_image.image.name+".png")
                            node_image.image.save_render(output_path)
                            
                            normal_texture_set.append(output_path)
        
                for node_image in nodes:
                    if node_image.type == 'TEX_IMAGE':
                        if (node_image == opacity_channel):
                            texture_path = bpy.path.abspath(node_image.image.filepath)
                            node_image.image.name = mesh_name + "_" + str(udim_index) + "_TEX_OPAC"
                            output_path = (folder_path + "\\" + node_image.image.name+".png")
                            node_image.image.save_render(output_path)
                            
                            opacity_texture_set.append(output_path)
                
                #texture_set.append(texture_list)
                
            new_material = bpy.data.materials.new(mesh_name+"_MAT")
            mesh_obj.data.materials[0] = new_material
            mesh_obj.data.materials.clear()
            mesh_obj.data.materials.append(new_material)
        
            new_material.use_nodes = True
            new_material.blend_method = "CLIP"
            
            node_tree = new_material.node_tree
            
            bsdf = None
            
            for node in node_tree.nodes:
                if node.type == 'BSDF_PRINCIPLED':
                    bsdf = node
            
            #diffuse
            if (len(diffuse_texture_set) > 0):
                diffuse_texture_node = node_tree.nodes.new('ShaderNodeTexImage')
                diffuse_texture_node.location = (-200, 0)
                diffuse_texture_node.image = bpy.data.images.load(diffuse_texture_set[0])
                diffuse_texture_node.image.source = "TILED"
                '''
                opacity_texture_node = node_tree.nodes.new('ShaderNodeTexImage')
                opacity_texture_node.location = (-200, -400)
                opacity_texture_node.image = bpy.data.images.load(diffuse_texture_set[0])
                opacity_texture_node.image.source = "TILED"
                '''
                links1 = node_tree.links
                links1.new(diffuse_texture_node.outputs['Color'], bsdf.inputs['Base Color'])
                links4 = node_tree.links
                links4.new(diffuse_texture_node.outputs['Alpha'], bsdf.inputs['Alpha'])
                
            #normal
            if (len(normal_texture_set) > 0):
                normal_map_node = node_tree.nodes.new('ShaderNodeNormalMap')
                normal_map_node.location = (-200, -200)
                
                normal_texture_node = node_tree.nodes.new('ShaderNodeTexImage')
                normal_texture_node.location = (-200, -200)
                normal_texture_node.image = bpy.data.images.load(normal_texture_set[0])
                normal_texture_node.image.source = "TILED"
                
                links2 = node_tree.links
                links2.new(normal_texture_node.outputs['Color'], normal_map_node.inputs['Color'])
                
                links3 = node_tree.links
                links3.new(normal_map_node.outputs['Normal'], bsdf.inputs['Normal'])
            '''
            #opacity
            if (len(opacity_texture_set) > 0):
                opacity_texture_node = node_tree.nodes.new('ShaderNodeTexImage')
                opacity_texture_node.location = (-200, -400)
                opacity_texture_node.image = bpy.data.images.load(opacity_texture_set[0])
                opacity_texture_node.image.source = "TILED"
                
                links4 = node_tree.links
                links4.new(opacity_texture_node.outputs['Color'], bsdf.inputs['Alpha'])
            '''
    
    def rename_shape_keys(self):
        for i in range(len(self.mesh_obj_list)):
            mesh_obj = self.mesh_obj_list[i]
            if mesh_obj.data.shape_keys is not None:
                shape_keys = mesh_obj.data.shape_keys.key_blocks
                if shape_keys is not None:
                    for k in self.expression_data:
                        for index, key in enumerate(shape_keys):
                            if key.name == self.expression_data[k]["Extend"]:
                                key.name = k
                            if key.name == self.expression_data[k]["Standard"]:
                                key.name = k
                            if key.name == self.expression_data[k]["ARKit"]:
                                key.name = k
                            if key.name == self.expression_data[k]["Tradition"]:
                                key.name = k
                            key.value = 0.0
    
    def reset_shape_keys(self):
        bpy.ops.object.mode_set(mode='OBJECT')
        for obj in bpy.data.objects:
            if obj.type == 'MESH' and obj.data.shape_keys is not None:
                shape_keys = obj.data.shape_keys

                for key_block in shape_keys.key_blocks:
                    key_block.value = 0.0
                    #key_block.keyframe_insert(data_path="value") 
    
    def merge_shape_keys(self, _a_shape, _b_shape, _new_shape):
        for i in range(len(self.mesh_obj_list)):
            mesh_obj = self.mesh_obj_list[i]
            if mesh_obj is not None and mesh_obj.type == "MESH":
                shape_keys = mesh_obj.data.shape_keys
                if shape_keys is not None:
                    if _a_shape in shape_keys.key_blocks and _b_shape in shape_keys.key_blocks:
                        aa_key = shape_keys.key_blocks[_a_shape]
                        bb_key = shape_keys.key_blocks[_b_shape]
                        
                        basis_key = shape_keys.key_blocks["Basis"]
        
                        new_key = mesh_obj.shape_key_add(name=_new_shape, from_mix=False)
                        
                        num_coords = len(aa_key.data)
        
                        for j in range(num_coords):
                            if aa_key.data[j] is not None and bb_key.data[j] is not None:
                                aa_coord = aa_key.data[j].co
                                bb_coord = bb_key.data[j].co
                                basis_coord = basis_key.data[j].co
                                
                                new_key.data[j].co = basis_coord + (aa_coord - basis_coord) + (bb_coord - basis_coord)
        
                        #shape_keys.key_blocks.remove(aa_key)
                        #shape_keys.key_blocks.remove(bb_key)
        
                        new_key.value = 0.0

    def create_stick_shape_keys(self):
        for i in range(len(self.mesh_obj_list)):
            mesh_obj = self.mesh_obj_list[i]

            if mesh_obj is not None and mesh_obj.type == "MESH":
                shape_keys = mesh_obj.data.shape_keys
                
                _MFUpL_shape = "Mouth_Funnel_Up_L"
                _MFUpR_shape = "Mouth_Funnel_Up_R"
                _MFDnL_shape = "Mouth_Funnel_Down_L"
                _MFDnR_shape = "Mouth_Funnel_Down_R"
                _MC_shape    = "Mouth_Close"
                
                if shape_keys is not None:
                    if _MFUpL_shape in shape_keys.key_blocks and _MFUpR_shape in shape_keys.key_blocks :
                        MFUpL_key = shape_keys.key_blocks[_MFUpL_shape]
                        MFUpR_key = shape_keys.key_blocks[_MFUpR_shape]
                        MFDnL_key = shape_keys.key_blocks[_MFDnL_shape]
                        MFDnR_key = shape_keys.key_blocks[_MFDnR_shape]
                        MC_key = shape_keys.key_blocks[_MC_shape]
                        
                        basis_key = shape_keys.key_blocks["Basis"]
        
                        LSL_new_key = mesh_obj.shape_key_add(name="lipStickyL", from_mix=False)
                        LSR_new_key = mesh_obj.shape_key_add(name="lipStickyR", from_mix=False)
                        
                        num_coords = len(basis_key.data)
        
                        for j in range(num_coords):
                            if MFUpL_key.data[j] is not None and MFDnL_key.data[j] is not None:
                                aa_coord = MFUpL_key.data[j].co
                                bb_coord = MFDnL_key.data[j].co
                                
                                aa1_coord = MFUpR_key.data[j].co
                                bb1_coord = MFDnR_key.data[j].co
                                
                                cc_coord = MC_key.data[j].co
                                
                                basis_coord = basis_key.data[j].co
                                
                                LSL_new_key.data[j].co = basis_coord + (aa1_coord - basis_coord)*0.5 + (bb1_coord - basis_coord)*0.5 + (cc_coord - basis_coord)*0.2
                                
                                LSR_new_key.data[j].co = basis_coord + (aa_coord - basis_coord)*0.5 + (bb_coord - basis_coord)*0.5 + (cc_coord - basis_coord)*0.2
        
                        #shape_keys.key_blocks.remove(aa_key)
                        #shape_keys.key_blocks.remove(bb_key)
        
                        LSL_new_key.value = 0.0
                        LSR_new_key.value = 0.0

    def assign_driver(self):
        armature = self.armature
        mesh_obj = self.shape_key_mesh
        
        if mesh_obj.data.shape_keys.key_blocks.get("jawOpen") == None:
            shape_key = mesh_obj.shape_key_add(name="jawOpen", from_mix=False)
        if mesh_obj.data.shape_keys.key_blocks.get("jawL") == None:
            shape_key = mesh_obj.shape_key_add(name="jawL", from_mix=False)
        if mesh_obj.data.shape_keys.key_blocks.get("jawR") == None:
            shape_key = mesh_obj.shape_key_add(name="jawR", from_mix=False)
        if mesh_obj.data.shape_keys.key_blocks.get("eyeUp") == None:
            shape_key = mesh_obj.shape_key_add(name="eyeUp", from_mix=False)
        if mesh_obj.data.shape_keys.key_blocks.get("eyeDn") == None:
            shape_key = mesh_obj.shape_key_add(name="eyeDn", from_mix=False)
        if mesh_obj.data.shape_keys.key_blocks.get("eyeL") == None:
            shape_key = mesh_obj.shape_key_add(name="eyeL", from_mix=False)
        if mesh_obj.data.shape_keys.key_blocks.get("eyeR") == None:
            shape_key = mesh_obj.shape_key_add(name="eyeR", from_mix=False)
        
        bpy.ops.object.mode_set(mode='POSE')
        
        jaw_open_bone = armature.pose.bones["CC_Base_JawRoot"]
        eye_L_bone = armature.pose.bones["CC_Base_L_Eye"]
        eye_R_bone = armature.pose.bones["CC_Base_R_Eye"]
        
        jaw_open_bone.rotation_mode = 'XYZ'
        eye_L_bone.rotation_mode = 'XYZ'
        eye_R_bone.rotation_mode = 'XYZ'
        
        # Jaw Open
        jOpen_driver = jaw_open_bone.driver_add("rotation_euler", 2)
        if len(jOpen_driver.driver.variables)==0:
            var = jOpen_driver.driver.variables.new()
            var.name = "JawOpen"  
            var.targets[0].id_type = 'KEY'
            shape_key = mesh_obj.data.shape_keys.key_blocks.get("jawOpen")
            var.targets[0].id = shape_key.id_data
            var.targets[0].data_path = f'key_blocks["jawOpen"].value'
        jOpen_driver.driver.expression = "JawOpen*0.5"
        
        # Jaw Left / Right
        jLR_driver = jaw_open_bone.driver_add("rotation_euler", 1)
        if len(jLR_driver.driver.variables)==0:
            var_L = jLR_driver.driver.variables.new()
            var_L.name = "Left"  
            var_L.targets[0].id_type = 'KEY'
            shape_key = mesh_obj.data.shape_keys.key_blocks.get("jawL")
            var_L.targets[0].id = shape_key.id_data
            var_L.targets[0].data_path = f'key_blocks["jawL"].value'
        
            var_R = jLR_driver.driver.variables.new()
            var_R.name = "Right"  
            var_R.targets[0].id_type = 'KEY'
            shape_key = mesh_obj.data.shape_keys.key_blocks.get("jawR")
            var_R.targets[0].id = shape_key.id_data
            var_R.targets[0].data_path = f'key_blocks["jawR"].value'
        
        jLR_driver.driver.expression = "Left*-0.5+Right*0.5"
        
        # Eye Left
        eye_L_x_driver = eye_L_bone.driver_add("rotation_euler", 0)
        if len(eye_L_x_driver.driver.variables)==0:
            var_L = eye_L_x_driver.driver.variables.new()
            var_L.name = "Up"  
            var_L.targets[0].id_type = 'KEY'
            shape_key = mesh_obj.data.shape_keys.key_blocks.get("eyeUp")
            var_L.targets[0].id = shape_key.id_data
            var_L.targets[0].data_path = f'key_blocks["eyeUp"].value'
        
            var_R = eye_L_x_driver.driver.variables.new()
            var_R.name = "Dn"  
            var_R.targets[0].id_type = 'KEY'
            shape_key = mesh_obj.data.shape_keys.key_blocks.get("eyeDn")
            var_R.targets[0].id = shape_key.id_data
            var_R.targets[0].data_path = f'key_blocks["eyeDn"].value'
        eye_L_x_driver.driver.expression = "Up*-0.5+Dn*0.5"
        
        eye_L_z_driver = eye_L_bone.driver_add("rotation_euler", 2)
        if len(eye_L_z_driver.driver.variables)==0:
            var_L = eye_L_z_driver.driver.variables.new()
            var_L.name = "Left"  
            var_L.targets[0].id_type = 'KEY'
            shape_key = mesh_obj.data.shape_keys.key_blocks.get("eyeL")
            var_L.targets[0].id = shape_key.id_data
            var_L.targets[0].data_path = f'key_blocks["eyeL"].value'
        
            var_R = eye_L_z_driver.driver.variables.new()
            var_R.name = "Right"  
            var_R.targets[0].id_type = 'KEY'
            shape_key = mesh_obj.data.shape_keys.key_blocks.get("eyeR")
            var_R.targets[0].id = shape_key.id_data
            var_R.targets[0].data_path = f'key_blocks["eyeR"].value'
        eye_L_z_driver.driver.expression = "Left*0.5+Right*-0.5"
    
        # Eye Right
        eye_R_x_driver = eye_R_bone.driver_add("rotation_euler", 0)
        if len(eye_R_x_driver.driver.variables)==0:
            var_L = eye_R_x_driver.driver.variables.new()
            var_L.name = "Up"  
            var_L.targets[0].id_type = 'KEY'
            shape_key = mesh_obj.data.shape_keys.key_blocks.get("eyeUp")
            var_L.targets[0].id = shape_key.id_data
            var_L.targets[0].data_path = f'key_blocks["eyeUp"].value'
        
            var_R = eye_R_x_driver.driver.variables.new()
            var_R.name = "Dn"  
            var_R.targets[0].id_type = 'KEY'
            shape_key = mesh_obj.data.shape_keys.key_blocks.get("eyeDn")
            var_R.targets[0].id = shape_key.id_data
            var_R.targets[0].data_path = f'key_blocks["eyeDn"].value'
        eye_R_x_driver.driver.expression = "Up*-0.5+Dn*0.5"
        
        eye_R_z_driver = eye_R_bone.driver_add("rotation_euler", 2)
        if len(eye_R_z_driver.driver.variables)==0:
            var_L = eye_R_z_driver.driver.variables.new()
            var_L.name = "Left"  
            var_L.targets[0].id_type = 'KEY'
            shape_key = mesh_obj.data.shape_keys.key_blocks.get("eyeL")
            var_L.targets[0].id = shape_key.id_data
            var_L.targets[0].data_path = f'key_blocks["eyeL"].value'
        
            var_R = eye_R_z_driver.driver.variables.new()
            var_R.name = "Right"  
            var_R.targets[0].id_type = 'KEY'
            shape_key = mesh_obj.data.shape_keys.key_blocks.get("eyeR")
            var_R.targets[0].id = shape_key.id_data
            var_R.targets[0].data_path = f'key_blocks["eyeR"].value'
        eye_R_z_driver.driver.expression = "Left*0.5+Right*-0.5"
        
        bpy.ops.object.mode_set(mode='OBJECT')

    def connect_shape_keys(self):
        
        for i in range(len(self.mesh_obj_list)):
            if self.mesh_obj_list[i] != self.shape_key_mesh:
                source_shape_keys = self.shape_key_mesh.data.shape_keys
                target_shape_keys = self.mesh_obj_list[i].data.shape_keys
                try:
                    for target_key_block in target_shape_keys.key_blocks:
                        key_name = target_key_block.name
                
                        if key_name in source_shape_keys.key_blocks:
            
                            driver = target_key_block.driver_add("value").driver
                            #driver.type = 'AVERAGE'
                            source_path = 'key_blocks["{}"].value'.format(key_name)
                            target_path = 'key_blocks["{}"].value'.format(key_name)
            
                            var = driver.variables.new()
                            var.name = 'var'
                            var.type = 'SINGLE_PROP'
                            var.targets[0].id_type = 'KEY'
                            var.targets[0].id = source_shape_keys
                            var.targets[0].data_path = source_path
                
                            driver.expression = 'var'
                except:
                    pass

    def change_bone_parent(self):
        bpy.ops.object.mode_set(mode='EDIT') 
        
        self.armature.data.edit_bones['Head'].parent = self.armature.data.edit_bones['Neck']
        self.armature.data.edit_bones['LeftUpLeg'].parent = self.armature.data.edit_bones['Hips']
        self.armature.data.edit_bones['RightUpLeg'].parent = self.armature.data.edit_bones['Hips']
        
        bpy.ops.object.mode_set(mode='OBJECT') 
            
    def create_collection_and_move_armature(self):
        '''
        armature = self.armature
        
        collection = bpy.data.collections.new("character")
        bpy.context.scene.collection.children.link(collection)
        
        obj_collection = self.armature.users_collection[0]
        obj_collection.objects.unlink(self.armature)
        collection.objects.link(self.armature)
        
        for i in range (len(self.mesh_obj_list)):
            mesh_obj = self.mesh_obj_list[i]
            obj_collection = mesh_obj.users_collection[0]
            obj_collection.objects.unlink(mesh_obj)
            collection.objects.link(mesh_obj)
        '''
        col = bpy.data.collections.get("Collection")
        col.name = "character"


def register():
    bpy.utils.register_class(CC2WonderAction)

def unregister():
    bpy.utils.unregister_class(CC2WonderAction)
