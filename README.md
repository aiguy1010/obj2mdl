Introduction
============
Since Urho3D currently does not allow .obj models to be imported natively, this
this project aims to expedited the process of converting .obj files to .mdl
files and adding them to a Urho3D project.

Requirements
============
* [Blender 3D](https://www.blender.org/): This will need to be available from
  the commandline as `blender`
* [Urho3D Blender add-on](https://github.com/reattiva/Urho3D-Blender): Instructions
  on how to install this can be found in that projects README

Usage
=====
To use this script, place this folder inside the Urho3D project directory (the
same directory that contains the `bin` folder). Place all `.obj` files that you
would like to add to your Urho3D project into the `objs` folder, and run,

    ./obj2mdl

in the same directory as this README. Converted .mdl will then be added to your
projects `bin/Data/Models` directory, and can be loaded into Urho3D using a
commands like,

    Node* myNode = scene_->CreateChild("SampleNode");
    myNode->SetPosition( Vector3(0.0f, 0.0f, 0.0f) );
    StaticModel* myObject = myNode->CreateComponent<StaticModel>();
    myObject->SetModel(cache->GetResource<Model>("Models/MyOldOBJ.mdl"));

NOTE: The `objs` folder included in this repository already contains a .obj of
the Blender monkey, Suzanne, as a sample. If you do not want this sample  added
to your Urho3D project's resources as a .mdl, you should remove it before
running `./obj2mdl`.
