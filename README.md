<!--/*
 * README.md
 * This file is part of FoI
 *
 * Copyright (C) 2024 - Raul Vilchez Ruiz
 *
 * FoI is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 2 of the License, or
 * (at your option) any later version.
 *
 * FoI is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with FoI. If not, see <http://www.gnu.org/licenses/>.
 */-->
## File of Interest

A bunch of files, that for some reason, they have
any interest to remark by itself.

Examples:

A README file that could be droped on diferent repositories, all
of those belonging to different projects. A LICENSE file, a 
bitacora file, whose mision is to log the commands or scripts
done while a work session.

All these files are a physical link of the original file and,
a control version file, with their appropriate log and history.

This repository could be used as per file, developer environment,
with the power of git. I'll put an example session:

1. cd this directory(FoI). The name could be whatever you want.

2. make a hard copy of the file of interest:
		ln -P --backup=numbered /path/to/file .

3. Write/modify the file.

4. When done with the file, take a look at git dradis, and 
update acordingly.

5. To stop pounding on the original file, just unlink it. After
this, the file will be ERASED from this repository, but, you can
count with git power if did it well. Dive with `git log -p hash`
to find in the history, data contined in the file, the last time
you saved the file with git.

		unlink my_file

### Config files
To start working with all this mesh, open your `~/.bashrc` and add
as easy alias `alias foiln='echo "ln -P --backup=numbered /path/to/file ."'`
It just remember the link command, when starting to pull files to the
repository. Reload bash with `source ~/.bashrc`, and you are done.

Conventionally, a repo is a directory down the user space;
		/home/user/myRepos/FoI/

If it is not done before, make a directroy under the `myRepos`
directory, and stablish the FoI dir.
1. `mkdir -p myRepos/FoI`.
2. `cd myRepos/FoI`.
3. `git init`.
4. Drop inside your static files; readme, license, whatever.
5. Use the dradis: 
		git status; git add FoI-file; git commit -m 'initial commit, Repo FoI.'
6. Now link the foi file. `ln -P --backup=numbered /path/to/file .`
7. In this case, i omited all that staff of my README because it's
specific of the repo FoI. I will start pounding on a original file
with a spec of a driver; yours could be anything. I don't have any
other place where this document is binded.

Next step; to stablish a quick copy of the File of Interest, so you
can count with a rapid backup of the file at the state you 'imported'
or hard linked the file. This is just to be save, it's not imperative
this step because the best scenario is to commit the file just once
hard linked. Any way; to do this: `cat foi-file > foi-file.bak`.
Remember, once unlinked the foi file, it'll be erased.

When the directory is just started, or few populated, it doesn't have
too many sense to make directories inside; the situation change with
the neighbourhood at the door. Just make a directory with descriptive
name; example: `myWonderfullApp/foi.files`.

Another usefull technique, consist in printing _a value of a symbolic_
_link or canonical file name._

__absolute path:__
		readlink -f foi.file 

__find all links of specific inode__
		stat foi.file
		find ~/ -inum inode_num


### Spec files

Specification files -or specs for short; are another example of those
files that not belonging to any particular project by itself, it's
binded to a development process.

This is slightly different of other wide used files, because relates
to specific projects, but is not part of the source that the developer
coded, to make 'usefull' their application.

I think a example session should be clear enough:
1. Pull the file to your foi repositorie.
2. Make changes on file, and save with your editor.
3. The changes made over the file could be a few ones, or numerous
changes. In this step, we'll prepare to planning what we'll do in the
source and how we'll document the work done.

I have some changes in my spec file, as: required dependencies, 
exclusive architecture decissions, and a few others.
Once the work is done, it appears the need to document all the task
done on the source -file spec. The problem in this repositorie it's
that it will sostain a bunch of unordered files, that could or could
not relate betwen them. So the question is; what kind of logs i want
to state in the history of this repo?

In my opinion, all anotations should be integrated on the git log
as a block. A general propouse log that describes all changes done
_in a row._
This avoids to duplicate the log, here; in the File of Interest repo,
and in the actual repo that reflects the development of the application.
In this way, it's possible to use this repo as an index of changes
done over specific files; the idea is to _cat_ the git log _grepping_
for a file.

		prompt:> git log --oneline |grep ckb-next.spec
		f4721f6 ckb-next.spec file, added to DVCS.

That was the the recovered log, once added to the repo.

		prompt:> git log --oneline |grep ckb-next.spec
		a9d509e ckb-next.spec. BuildRequires, pre, quickinstall erased.
		f4721f6 ckb-next.spec file, added to DVCS.

This time, i added a summary line, that reflects changes done
over the file. It doesn't matter if it is deleted the file;
because those changes are part of the git log history, and it's
posssible to retrive that data in a single log.

The oposite situation appears on the actual repo of the project,
where a more grained description of each change should be done.
In this case the spec file -as i said before, is not part of the
source, but if i need to do so, now i have a _guide_ where to start
documenting each chunk of data change; `git add -i` on the development
repo of the application, will be suffice to _patch_ each minimal change.


### Bitacora files
### LICENSE files
### README files
### Git ignores


