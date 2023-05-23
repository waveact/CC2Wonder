# CC2Wonder
Converting Reallusion CC characters to be compatible with the Wonder Studio platform.  
(Currently, it is not fully refined, and there are often errors that require manual debugging.)  

**Workflow Video**  
https://youtu.be/mE5Afw7Z44w

**Supported Version**  
- Blender 3.4 **(DO NOT USE 3.5)**
- Character Creator 4.22 above  

**Supported Assets**  
- FBX files exported from CC4.  
- The Character with a single mesh and material.  
- Facial profile data is CC4 Extend.  

**How to Install**  
In Blender, Edit > Preferences > Add-ons > Install > Choose the zip file download from this repository 

**Support Character Source**    
1. CC3+ character  
2. [actorSCAN](https://www.reallusion.com/content/characterspec/)
3. [actorBUILD](https://www.reallusion.com/content/characterspec/)  

**How to Export**
1. Apply T-Pose Pose from Content Manager.  
2. Export an FBX file from CC4 using the **Blender preset**. Make sure  
- Uncheck the "Embed Texture" option.  
- Choose "Current Pose".
- Uncheck the "First Frame in Bind Pose".  
- Enable the "Delete Hidden Mesh".   
- Enable the "Merge Opacity into Diffuse Map"  
3. Open Blender and import the FBX file. Select the **Armature** and go to **Tool > CC2Wonder > Export to Wonder**. Choose your favorite folder and enter the desired file name.  
4. Once the process is complete, you will find the generated .blend file and the associated textures in the folder you selected. You can now upload those files to Wonder Studio for further use.  

