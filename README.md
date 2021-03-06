Introduction
============
Since Urho3D currently does not allow .obj models to be imported natively, this
this project aims to expedite the process of converting .obj files to .mdl
files and adding them to an Urho3D project.

Requirements
============
* [Blender 3D](https://www.blender.org/): This will need to be available from
  the command-line as `blender`. On Windows this will mean adding the Blender
  install directory to your PATH environment variable.
* [Urho3D Blender add-on](https://github.com/reattiva/Urho3D-Blender): Instructions
  on how to install can be found in add-on project's README

Usage
=====
Place this folder inside the Urho3D project directory (the
same directory that contains the `bin` folder). Place all `.obj` files that you
would like to add to your Urho3D project into the `objs` folder, and, in the  
same folder as this README, run,

Linux:

    ./obj2mdl


Windows:

    obj2mdl.bat


Converted .mdl will then be added to your project's `bin/Data/Models` directory,
and can be loaded into Urho3D using code like,

    Node* myNode = scene_->CreateChild("SampleNode");
    myNode->SetPosition( Vector3(0.0f, 0.0f, 0.0f) );
    StaticModel* myObject = myNode->CreateComponent<StaticModel>();
    myObject->SetModel(cache->GetResource<Model>("Models/MyOldOBJ.mdl"));

NOTE: The `objs` folder included in this repository already contains a .obj of
the Blender monkey, Suzanne, as a sample. If you do not want this sample  added
to your Urho3D project's resources as a .mdl, you should remove it before
running `./obj2mdl`.
