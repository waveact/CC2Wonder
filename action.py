import bpy
import os

class CC2WonderAction(bpy.types.Operator):
    bl_idname = "object.cc2wonder_action"
    bl_label = "Save"
    
    filepath: bpy.props.StringProperty(subtype="FILE_PATH")
    
    def execute(self, context):
        addon_path = os.path.dirname(os.path.realpath(__file__))
        resource_path = os.path.join(addon_path, "resource")

        armature_name = "Armature"
        armature = bpy.data.objects.get(armature_name)
        armature.name = "CC_BODY"
        
        self.armature = armature
        
        self.mesh_name = "CCMesh"
        
        self.udim = {"1001":"Head", "1002":"Body", "1003":"Arm", "1004":"Leg", "1005":"Nail", "1006":"Eyalash"}
        
        filepath = bpy.path.abspath(self.filepath)
        self.folder_path = os.path.dirname(filepath)
        
        self.convert_bone_data = {"CC_Base_L_Clavicle":"LeftShoulder","CC_Base_L_Upperarm":"LeftArm","CC_Base_L_Forearm":"LeftForeArm","CC_Base_L_Hand":"LeftHand","CC_Base_L_Thumb1":"LeftHandThumb1","CC_Base_L_Thumb2":"LeftHandThumb2","CC_Base_L_Thumb3":"LeftHandThumb3","CC_Base_L_Index1":"LeftHandIndex1","CC_Base_L_Index2":"LeftHandIndex2","CC_Base_L_Index3":"LeftHandIndex3","CC_Base_L_Mid1":"LeftHandMiddle1","CC_Base_L_Mid2":"LeftHandMiddle2","CC_Base_L_Mid3":"LeftHandMiddle3","CC_Base_L_Ring1":"LeftHandRing1","CC_Base_L_Ring2":"LeftHandRing2","CC_Base_L_Ring3":"LeftHandRing3","CC_Base_L_Pinky1":"LeftHandPinky1","CC_Base_L_Pinky2":"LeftHandPinky2","CC_Base_L_Pinky3":"LeftHandPinky3","CC_Base_L_Thigh":"LeftUpLeg","CC_Base_L_Calf":"LeftLeg","CC_Base_L_Foot":"LeftFoot","CC_Base_L_ToeBase":"LeftToeBase","CC_Base_R_Clavicle":"RightShoulder","CC_Base_R_Upperarm":"RightArm","CC_Base_R_Forearm":"RightForeArm","CC_Base_R_Hand":"RightHand","CC_Base_R_Thumb1":"RightHandThumb1","CC_Base_R_Thumb2":"RightHandThumb2","CC_Base_R_Thumb3":"RightHandThumb3","CC_Base_R_Index1":"RightHandIndex1","CC_Base_R_Index2":"RightHandIndex2","CC_Base_R_Index3":"RightHandIndex3","CC_Base_R_Mid1":"RightHandMiddle1","CC_Base_R_Mid2":"RightHandMiddle2","CC_Base_R_Mid3":"RightHandMiddle3","CC_Base_R_Ring1":"RightHandRing1","CC_Base_R_Ring2":"RightHandRing2","CC_Base_R_Ring3":"RightHandRing3","CC_Base_R_Pinky1":"RightHandPinky1","CC_Base_R_Pinky2":"RightHandPinky2","CC_Base_R_Pinky3":"RightHandPinky3","CC_Base_R_Thigh":"RightUpLeg","CC_Base_R_Calf":"RightLeg","CC_Base_R_Foot":"RightFoot","CC_Base_R_ToeBase":"RightToeBase","CC_Base_Head":"Head","CC_Base_NeckTwist01":"Neck","CC_Base_Spine02":"Spine2","CC_Base_Spine01":"Spine1","CC_Base_Waist":"Spine","CC_Base_Hip":"Hips","RL_BoneRoot":"root"}

        self.convert_data = {"browInnerDnL":{"Extend":"Brow_Drop_L","Standard":"Brow_Drop_L"},"browInnerDnR":{"Extend":"Brow_Drop_R","Standard":"Brow_Drop_R"},"browInnerUpL":{"Extend":"Brow_Raise_Inner_L","Standard":"Brow_Raise_Inner_L"},"browInnerUpR":{"Extend":"Brow_Raise_Inner_R","Standard":"Brow_Raise_Inner_R"},"browOuterDnL":{"Extend":"","Standard":""},"browOuterDnR":{"Extend":"","Standard":""},"browOuterUpL":{"Extend":"Brow_Raise_Outer_L","Standard":"Brow_Raise_Outer_L"},"browOuterUpR":{"Extend":"Brow_Raise_Outer_R","Standard":"Brow_Raise_Outer_R"},"browSqueezeL":{"Extend":"Brow_Compress_L","Standard":""},"browSqueezeR":{"Extend":"Brow_Compress_R","Standard":""},"cheekBlowL":{"Extend":"Cheek_Puff_L","Standard":"Cheek_Puff_L"},"cheekBlowR":{"Extend":"Cheek_Puff_R","Standard":"Cheek_Puff_R"},"cheekUpL":{"Extend":"Cheek_Raise_L","Standard":"Cheek_Raise_L"},"cheekUpR":{"Extend":"Cheek_Raise_R","Standard":"Cheek_Raise_R"},"eyeBlinkL":{"Extend":"Eye_Blink_L","Standard":"Eye_Blink_L"},"eyeBlinkR":{"Extend":"Eye_Blink_R","Standard":"Eye_Blink_R"},"eyeCompressL":{"Extend":"Cheek_Raise_L","Standard":"Cheek_Raise_L"},"eyeCompressR":{"Extend":"Cheek_Raise_R","Standard":"Cheek_Raise_R"},"eyeDn":{"Extend":"Eye_Look_Down","Standard":"Eye_Look_Down"},"eyeL":{"Extend":"Eye_Look_L","Standard":"Eye_Look_L"},"eyeR":{"Extend":"Eye_Look_R","Standard":"Eye_Look_R"},"eyeSquintL":{"Extend":"Eye_Squint_L","Standard":"Eye_Squint_L"},"eyeSquintR":{"Extend":"Eye_Squint_R","Standard":"Eye_Squint_R"},"eyeUp":{"Extend":"Eye_Look_Up","Standard":"Eye_Look_Up"},"eyeWidenLowerL":{"Extend":"","Standard":""},"eyeWidenLowerR":{"Extend":"","Standard":""},"eyeWidenUpperL":{"Extend":"Eye_Wide_L","Standard":"Eye_Wide_L"},"eyeWidenUpperR":{"Extend":"Eye_Wide_R","Standard":"Eye_Wide_R"},"jawClenchL":{"Extend":"","Standard":""},"jawClenchR":{"Extend":"","Standard":""},"jawIn":{"Extend":"Jaw_Backward","Standard":""},"jawL":{"Extend":"Jaw_L","Standard":"Jaw_L"},"jawOpen":{"Extend":"Jaw_Open","Standard":"Jaw_Open"},"jawOut":{"Extend":"Jaw_Forward","Standard":"Jaw_Forward"},"jawR":{"Extend":"Jaw_R","Standard":"Jaw_R"},"lipChinRaiserL":{"Extend":"","Standard":""},"lipChinRaiserR":{"Extend":"","Standard":""},"lipCloseLower":{"Extend":"","Standard":""},"lipCloseUpper":{"Extend":"","Standard":""},"lipCornerDnL":{"Extend":"Mouth_Frown_L","Standard":"Mouth_Frown_L"},"lipCornerDnR":{"Extend":"Mouth_Frown_R","Standard":"Mouth_Frown_R"},"lipCornerUpL":{"Extend":"Mouth_Smile_Sharp_L","Standard":""},"lipCornerUpR":{"Extend":"Mouth_Smile_Sharp_R","Standard":""},"lipDimplerL":{"Extend":"Mouth_Dimple_L","Standard":"Mouth_Dimple_L"},"lipDimplerR":{"Extend":"Mouth_Dimple_R","Standard":"Mouth_Dimple_R"},"lipFunnelerLower":{"Extend":"","Standard":""},"lipFunnelerUpper":{"Extend":"","Standard":""},"lipLowerDnL":{"Extend":"Mouth_Roll_Out_Lower_L","Standard":""},"lipLowerDnR":{"Extend":"Mouth_Roll_Out_Lower_R","Standard":""},"lipLowerPullDnL":{"Extend":"Mouth_Pull_Lower_L","Standard":""},"lipLowerPullDnR":{"Extend":"Mouth_Pull_Lower_R","Standard":""},"lipLowerUpL":{"Extend":"Mouth_Roll_In_Lower_L","Standard":""},"lipLowerUpR":{"Extend":"Mouth_Roll_In_Lower_R","Standard":""},"lipNarrowL":{"Extend":"","Standard":""},"lipNarrowR":{"Extend":"","Standard":""},"lipPoutLower":{"Extend":"","Standard":""},"lipPoutUpper":{"Extend":"","Standard":""},"lipPresserL":{"Extend":"Mouth_Press_L","Standard":"Mouth_Press_L"},"lipPresserR":{"Extend":"Mouth_Press_R","Standard":"Mouth_Press_R"},"lipPucker":{"Extend":"","Standard":""},"lipPullL":{"Extend":"Mouth_Lower_L","Standard":"Mouth_Lower_L"},"lipPullR":{"Extend":"Mouth_Lower_R","Standard":"Mouth_Lower_R"},"lipPushLower":{"Extend":"","Standard":""},"lipPushUpper":{"Extend":"","Standard":""},"lipSmileClosedL":{"Extend":"Mouth_Smile_L","Standard":""},"lipSmileClosedR":{"Extend":"Mouth_Smile_R","Standard":""},"lipSmileOpenL":{"Extend":"","Standard":""},"lipSmileOpenR":{"Extend":"","Standard":""},"lipSneerL":{"Extend":"","Standard":""},"lipSneerR":{"Extend":"","Standard":""},"lipStickyL":{"Extend":"","Standard":""},"lipStickyR":{"Extend":"","Standard":""},"lipSuckLower":{"Extend":"","Standard":""},"lipSuckUpper":{"Extend":"","Standard":""},"lipSwingL":{"Extend":"Mouth_L","Standard":"Mouth_L"},"lipSwingR":{"Extend":"Mouth_R","Standard":"Mouth_R"},"lipTightnerL":{"Extend":"Mouth_Tighten_L","Standard":""},"lipTightnerR":{"Extend":"Mouth_Tighten_R","Standard":""},"lipUpperDnL":{"Extend":"","Standard":""},"lipUpperDnR":{"Extend":"","Standard":""},"lipUpperUpL":{"Extend":"Mouth_Up_Upper_L","Standard":"Mouth_Up_Upper_L"},"lipUpperUpR":{"Extend":"Mouth_Up_Upper_R","Standard":"Mouth_Up_Upper_R"},"lipWidenL":{"Extend":"","Standard":""},"lipWidenR":{"Extend":"","Standard":""},"noseCompress":{"Extend":"","Standard":""},"noseFlare":{"Extend":"","Standard":""},"noseSneerL":{"Extend":"Nose_Sneer_L","Standard":"Nose_Sneer_L"},"noseSneerR":{"Extend":"Nose_Sneer_R","Standard":"Nose_Sneer_R"},"noseWrinklerL":{"Extend":"Nose_Crease_L","Standard":""},"noseWrinklerR":{"Extend":"Nose_Crease_R","Standard":""}}
   
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
        
        self.reset_shape_keys()
        
        self.rename_bones()
        self.change_bone_parent()
        
        self.rename_mesh()
        self.build_material()
        
        self.merge_shape_keys("Eye_L_Look_L", "Eye_R_Look_L", "eyeL")
        self.merge_shape_keys("Eye_L_Look_R", "Eye_R_Look_R", "eyeR")
        self.merge_shape_keys("Eye_L_Look_Up", "Eye_R_Look_Up", "eyeUp")
        self.merge_shape_keys("Eye_L_Look_Down", "Eye_R_Look_Down", "eyeDn")
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
        
        self.reset_shape_keys()
        
        self.create_collection_and_move_armature()
        
        if not filepath.lower().endswith(".blend"):
            filepath += ".blend"

        bpy.ops.wm.save_as_mainfile(filepath=filepath)
        
        self.report({'INFO'}, "Export CC Character to Wonder")
        
        return {'FINISHED'}
  
    def invoke(self, context, event):
        context.window_manager.fileselect_add(self)
        return {'RUNNING_MODAL'}

    
    def rename_bones(self):
        bpy.ops.object.mode_set(mode='POSE')
       
        for name in self.convert_bone_data:
            # get the pose bone with name
            bone = self.armature.pose.bones.get(name)
            # continue if no bone of that name
            if bone is None:
                continue
            # rename
            bone.name = self.convert_bone_data[name]
            
        bpy.ops.object.mode_set(mode='OBJECT')
    
    def rename_mesh(self):
        if len(self.mesh_obj_list) == 1:
            self.mesh_obj_list[0].name = self.mesh_name + "_FACE"
            self.mesh_obj_list[0].data.name = self.mesh_name
            self.shape_key_mesh = self.mesh_obj_list[0]
        
        for i in range(len(self.mesh_obj_list)):
            if self.mesh_obj_list[i].name == "CC_Base_Body":
                self.mesh_obj_list[i].name = self.mesh_name + "_Base_FACE"
                self.mesh_obj_list[i].data.name = self.mesh_name + "_Base"
                self.shape_key_mesh = self.mesh_obj_list[i]
    
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
                        diffuse_channel = bsdf.inputs["Base Color"].links[0].from_node
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
        mesh_obj = self.shape_key_mesh
        shape_keys = mesh_obj.data.shape_keys.key_blocks
        for k in self.convert_data:
            for index, key in enumerate(shape_keys):
                if key.name == self.convert_data[k]["Extend"]:
                    key.name = k
                if key.name == self.convert_data[k]["Standard"]:
                    key.name = k
                key.value = 0.0
    
    def reset_shape_keys(self):
        bpy.ops.object.mode_set(mode='OBJECT')
        for obj in bpy.data.objects:
            if obj.type == 'MESH' and obj.data.shape_keys is not None:
                shape_keys = obj.data.shape_keys

                for key_block in shape_keys.key_blocks:
                    key_block.value = 0.0
                    key_block.keyframe_insert(data_path="value") 
    
    def merge_shape_keys(self, _a_shape, _b_shape, _new_shape):
        mesh_obj = self.shape_key_mesh 
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
        mesh_obj = self.shape_key_mesh
        if mesh_obj is not None and mesh_obj.type == "MESH":
            shape_keys = mesh_obj.data.shape_keys
            
            _MFUpL_shape = "Mouth_Funnel_Up_L"
            _MFUpR_shape = "Mouth_Funnel_Up_R"
            _MFDnL_shape = "Mouth_Funnel_Down_L"
            _MFDnR_shape = "Mouth_Funnel_Down_R"
            _MC_shape    = "Mouth_Close"
            
            if shape_keys is not None:
                if _MFUpL_shape in shape_keys.key_blocks and _MFUpR_shape in shape_keys.key_blocks:
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
