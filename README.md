# CC2Wonder
Converting Reallusion CC characters to be compatible with the Wonder Studio platform.  
(Currently, it is not fully refined, and there are often errors that require manual debugging.)  

**Workflow Video**  
https://youtu.be/mE5Afw7Z44w

**Supported Version**  
- Blender 3.4 above  
- Character Creator 4.22 above  

**Supported Assets**  
- FBX files exported from CC4.  
- The Character with a single mesh and material.  
- Facial profile data is CC4 Extend.  

**How to Install**  
In Blender, Edit > Preferences > Add-ons > Install > Choose the py file download from this repository 

**Data Checking in Character Creator 4**  
- Character Source:  
Load CC3+ or [actorSCAN](https://www.reallusion.com/content/characterspec/), [actorBUILD](https://www.reallusion.com/content/characterspec/) character into [Character Creator 4](https://www.reallusion.com/character-creator/)  

- Facial Data:  
-- CC3+, by default, should be CC4 Extend. You don't need to do anything. If not, you can apply the CC4 Extend profile from the Content Manager.  
-- actorSCAN or actorBUILD, if the data is not in CC4 Extend format, you will need to convert it using the [Facial Profile Editor](https://courses.reallusion.com/home/character-creator/motion-pose-and-facial-expression?v=character-creator-4-tutorial-getting-started-with-cc4-facial-profiles-and-upgrading-cc3-characters).  

**How to Export**
1. Export an FBX file from CC4 using the **Blender preset**. Make sure to uncheck the "Embed Texture" option.  
2. Open Blender and import the FBX file. Select the **Armature** and go to **Tool > CC2Wonder > Export to Wonder**. Choose your favorite folder and enter the desired file name.  
3. Once the process is complete, you will find the generated .blend file and the associated textures in the folder you selected. You can now upload those files to Wonder Studio for further use.  

