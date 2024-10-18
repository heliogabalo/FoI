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


__Files with the same name__




### Spec files

Specification files -or specs for short; are another example of those
files that not belonging to any particular project by itself, it's
binded to a development process.

This is slightly different of other wide used files, because relates
to specific projects, but is not part of the source that the developer
coded, to make 'usefull' their application.

I think a example session should be clear enough:
1. Pull the file to your foi repository .
2. Make changes on file, and save with your editor.
3. The changes made over the file could be a few ones, or numerous
changes. In this step, we'll prepare to planning what we'll do in the
source and how we'll document the work done.

I have some changes in my spec file, as: required dependencies, 
exclusive platform decissions, and a few others.
Once the work is done, it appears the need to document all the task
done on the source -file spec. The problem in this repository  it's
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
In this case the spec file -as mentioned before, is not part of the
source, but if needed to do so, now there are a _guide_ where to start
documenting each chunk of data change; `git add -i` on the development
repo of the application, will be suffice to _patch_ each minimal change.


__Patching with bash__

"Patches are important because they allow you to start 
with pristine sources..."
	> extract from 'RPM 4 RPM guide'.
	
The first thing to do is to fetch the file on the FoI repo,
now start coding and making changes. 

		ln -P --backup=numbered /path/to/file .

Example scripting:
prompt:> cp original.h modified.h
prompt:> diff -u original.h modified.h > modified.patch
prompt:> patch patched.h modified.patch

File extension `.patch` is omited inside a `.gitigone` file, so could
be ereased or moved to modified.v1.0.0-1 on a repository.
Version is the relevant word, where the actual number represents a
change on the repository.

__Warning:__ with file backups, this technique of hard-linking files
is a process silently dangerous, you should not link any file.bak
or the state of the file will change without notice.

__Parches__
El concepto de parche en git, en mi opinión, resulta algo contradictorio
a lo que se entiende por hacer un parche, a uno o mas archivos, no
asociados a un repositorio. Pienso que rara vez resulta conveniente 
mezclar las técnica utilizadas. 
¿Para qué resulta útil un parche en git? Todos los commits en git, son
parches. Modificaciones que se han ido realizando a lo largo del 
desarrollo de uno o más archivos de fuente.
La excepción sería en un contexto donde no hay conexión al servidor git;
tal y como explican los distintos manuales(bundle, format-patch ...)
Es posible que por esta razón no haya sido implementado un mecanismo
equivalente en git(comando `diff/patch`). 
Los dos comandos antes mencionados; bundle y format-patch, son preparados
git, que aplican un formato específico para enviar vía correo electrónico
el commit elegido. Ninguno de ellos resulta en un archivo propiamente
de parche; una vez generado el archivo de cambio, debe recuperarse
con una herramienta específica de git. En este caso `git am`.

Por eso lo de no mezclar: 
		diff -u keymap.h patched-kmap.h > keymap.h.patch

		
__Patching with git__

		#### git-format git bundle
		## From HEAD count numbered of indexed commits
		git format-patch -k --stdout HEAD -1
		## From hash count numbered of indexed commits
		git format-patch -k --stdout hash -1 > file-git.patch
		## From hash to hash print those commits
		git format-patch -k --stdout hash..hash


		git mailinfo msg patch < mail >info
		git mailinfo msg patch-git.spec < git.patch

__Cherry picking__

This command `git cherry-pick` is used to apply the changes done in
one  commit on a given  repository, to  a clean  working tree (no
modifications from the HEAD commit). This is particularly interesting
to a FoI repo, where you can commit miskates, or unwanted changes, and 
re-commit your work without disturbing shared work.

		prompt:> git status 
		# On branch master
		# Changes to be committed:
		#   (use "git reset HEAD <file>..." to unstage)
		#
		#	new file:   keymap.h
		#	new file:   structures.h
		#
		# Changes not staged for commit:
		#   (use "git add <file>..." to update what will be committed)
		#   (use "git checkout -- <file>..." to discard changes in working directory)
		#
		#	modified:   README.md
		#

Option `-x` appends a line indicating the original commit that points to.
`git help cherry-pick`: 
	'Do not use this option if you are cherry-picking from your private
branch' -FoI in this case. Well, this is a special 'branch',
i'ts a repository that sources files from any given repository,
but it is not a canonical branch of any, it is a File of Interest: a bunch
of files, that for some reason, they have any interest to remark by itself.

Repos like this, can be used as index. It's not a repo that anyone will
erease; a branch in a delovopement scenario could continue or not.
This repository is a kind of place where the owner can drop files of
interest. 

It's sostainable without any file; the logs are always there. Git knowledge
spokes about this as "git history". Wonderfull, 

This convention conflicts with lines above, a banned degree and others
trains of, can appear from a user perspective. Several ways to avoid
this conflicts are known on replicating commands as `rpm -q pkg`; a
trivial example to query in some way, _what_ and _what not,_ can be do it.

__Note:__ Plese, don't call FoI anything; it's extrange as green dog.

### Bitacora files
### LICENSE files
### README files
### Git ignores


