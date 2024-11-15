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
 
## Table of contents

1. File of Interest
	1.99 Default branches.
	1.98 Git stash.
2. Config files
3. Spec files
4. Bitacora files
5. LICENSE files
6. README files
7. Git ignores
 
 
## 1. File of Interest

A bunch of files, that for some reason, they have any interest to
remark by itself.

Examples:

A README file that could be dropped on different repositories, all
of those belonging to different projects. A LICENSE file, a 
bitacora file, whose mission is to log the commands or scripts
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
update accordingly.

5. To stop pounding on the original file, just unlink it. After
this, the file will be ERASED from this repository, but, you can
count with git power if did it well. Dive with `git log -p hash`
to find in the history, data contained in the file, the last time
you saved the file with git.

		unlink my_file


## 1.99 Default branches

There are four _main_ branches on long-running projects; __master__,
__next__, __seen__, __maint__. The structure of the project, reflects
a complicated scenario, where a high number of developers and other
people, contribute to code development.

This is never the case of this repository; although the functionality
shown in a big project, could be applied here. The next movement 
should be to planning the names of the branches, and what propose
they will have.

Each topic branch, would may have a descriptive name, that speak
about the application, instead. In this way, the branch will take
the name of the project the developer is working on, and it avoids
to use regular names, as devel or develop branch, that have few
meaning here, since the repo by their own, is a development environment.

With that approach, there is no need to make a _new dir_ when adding
new files, that it doesn't belong to the same project. Simply checkout
to the specific branch, without bothering with unrelated files 
surfing in the working tree.

What will be the initial state of a new branch?
The state of the HEAD in the repo (clean working tree, obviously).
This notes just try to remark, that if was followed the rules
defined in the present document, a new branch will looks like as
your master branch, as expected, and it will be very easy to just
delete all content on the new branch, and start coding with the
specific task.

Example session:

1. git checkout -b myBranch
2. git rm $CLONED_FILES
3. git commit -m ''

warning here: about to save some file opened on the editor, when
branching without those files.

## 1.98 Git stash

"It takes the dirty state of your working directory, and saves it on
a stack of unfinished changes, that can reapply at any time -even on a
different branch". That is:

- modified tracked files, and
- staged changes.

		git stash save 'descriptive message of the task.'
		git stash		

Both commands accomplish almost the same; the decision to run one or
the other, depends on how many time, you expect to complete or 
retake the work undone. In a near future situation, it's acceptable
to enchant the shell with the abbreviated one. Can you say the same
in a delayed situation, where the 'x' is two hours, two days or maybe
a week?

### 2. Config files
To start working with all this mesh, open your `~/.bashrc` and add
as easy alias `alias foiln='echo "ln -P --backup=numbered /path/to/file ."'`
It just remember the link command, when starting to pull files to the
repository. Reload bash with `source ~/.bashrc`, and you are done.

Conventionally, a repo is a directory down the user space;
		/home/user/myRepos/FoI/

If it is not done before, make a directory under the `myRepos`
directory, and establish the FoI dir.
1. `mkdir -p myRepos/FoI`.
2. `cd myRepos/FoI`.
3. `git init`.
4. Drop inside your static files; readme, license, whatever.
5. Use the dradis: 
		git status; git add FoI-file; git commit -m 'initial commit, Repo FoI.'
6. Now link the foi file. `ln -P --backup=numbered /path/to/file .`
7. In this case, i omitted all that staff of my README because it's
specific of the repo FoI. I will start pounding on a original file
with a spec of a driver; yours could be anything. I don't have any
other place where this document is bonded.

Next step; to establish a quick copy of the File of Interest, so you
can count with a rapid backup of the file at the state you 'imported'
or hard linked the file. This is just to be save, it's not imperative
this step because the best scenario is to commit the file just once
hard linked. Any way; to do this: `cat foi-file > foi-file.bak`.
Remember, once unlinked the foi file, it'll be erased.

When the directory is just started, or few populated, it doesn't have
too many sense to make directories inside; the situation change with
the neighborhood at the door. Just make a directory with descriptive
name; example: `myWonderfullApp/foi.files`.

Another useful technique, consist in printing _a value of a symbolic_
_link or canonical file name._

__absolute path:__
		readlink -f foi.file 

__find all links of specific inode__
		stat foi.file
		find ~/ -inum inode_num


### 3. Spec files

Specification files -or specs for short; are another example of those
files that not belonging to any particular project by itself, it's
bonded to a development process.

This is slightly different of other wide used files, because relates
to specific projects, but is not part of the source that the developer
coded, to make 'useful' their application.

I think a example session should be clear enough:
1. Pull the file to your foi repository .
2. Make changes on file, and save with your editor.
3. The changes made over the file could be a few ones, or numerous
changes. In this step, we'll prepare to planning what we'll do in the
source and how we'll document the work done.

I have some changes in my spec file, as: required dependencies, 
exclusive platform decisions, and a few others.
Once the work is done, it appears the need to document all the task
done on the source -file spec. The problem in this repository  it's
that it will sustain a bunch of unordered files, that could or could
not relate between them. So the question is; what kind of logs i want
to state in the history of this repo?

In my opinion, all annotations should be integrated on the git log
as a block. A general propose log that describes all changes done
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
possible to retrieve that data in a single log.

The opposite situation appears on the actual repo of the project,
where a more grained description of each change should be done.
In this case the spec file -as mentioned before, is not part of the
source, but if needed to do so, now there are a _guide_ where to start
documenting each chunk of data change; `git add -i` on the development
repo of the application, will be suffice to _patch_ each minimal change.


__Patches__

There are methods to patch files as the tools used on a regular shell,
like Bash, and then, other methods; that package the hunks of code,
into an email envelop, to send those patches. Distributed version
control system, Git(DVCS).

Why is it useful a patch in git? All commits in git are patches.
Modifications that have been made, throughout the development of any
number of source files.

For various reasons it could appear the need to _transport_ a patch
from `computer-A` to `computer-B`. The conventional way of doing this,
is through the commands available in git. Now let's discuss about
a situation where _computer-B_ is inevitably offline.

In this context will be extracted a commit or more; a copy of the
commit message and their content, from the history of the repository.
Before sending the patch, it must be applied a format to the file
that works with the API.

A usual way of doing this, is via mail, storage device(USB).

		git 


En este contexto, extraer el contenido de dicha validación, pasa por
aplicar a los datos un formato específico, para que de alguna manera,
pueda ser trasladado; vía mail, via medio de almacenamiento.
Es posible que por esta razón haya sido implementado un mecanismo
equivalente en git(comando `diff/patch`). 


La excepción sería en un contexto donde no
hay conexión al servidor git; tal y como explican los distintos
manuales(bundle, format-patch ...).


Los dos comandos antes mencionados; bundle y format-patch, son preparados
git, que aplican un formato específico para enviar vía correo electrónico
el commit elegido. Ninguno de ellos resulta en un archivo propiamente
de parche; una vez generado el archivo de cambio, debe recuperarse
con una herramienta específica de git. En este caso `git am`.

Por eso lo de no mezclar: 
		scripting-prompt:> diff -u keymap.h patched-kmap.h > keymap.h.patch
con:
		git-prompt:>git format-patch -k --stdout HEAD -1

Este script es el código que se utilizaría en la .spec, para aplicar
los cambios de un parche:`Scripts/apply-patches.sh`.
		
		
Es posible utilizar ambos mecanismos en un único archivo de 
especificación, pero no mezclar los comandos. Cuando se trabaja en
una fuente con git, lo más razonable, es seguir utilizando esta 
herramienta, para producir y aplicar los parches. Si por el contrario,
el archivo proviene de una fuente externa a git; resutará conveniente
utilizar las técnicas de parcheado habitual.


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

File extension `.patch` is omitted inside a `.gitigone` file, so could
be erased or moved to modified.v1.0.0-1 on a repository.
Version is the relevant word, where the actual number represents a
change on the repository.


__Patching with git__

		#### format-patch, mailinfo, am, bundle, cherry-picking
		## From HEAD count numbered of indexed commits
		git format-patch -k --stdout HEAD -1
		## From hash count numbered of indexed commits
		git format-patch -k --stdout hash -1 > file-git.patch
		## From hash to hash print those commits
		git format-patch -k --stdout hash..hash


		git mailinfo msg patch < mail >info
		git mailinfo msg patch-git.spec < git.patch



This is a trick to use git patching engine, instead the usual scripting
with `patch`.

		%prep
		%setup -q
		# Create a git repo within the expanded tarball.
		git init
		git config user.email ""
		git config user.name ""
		git add .
		git commit -a -q -m "%{version} baseline."
		# Apply all the patches on top.
		git am %{patches}

The former directive inside a rpm specification file, is `PatchN:` 
where `N` is a number; consecutive or not.
With this trick it's used the rpm placeholder, but not the directive
since `git am` expects a list of files, with specific git patching 
format, as builded by the `git format-patch`.

__Cherry picking__

This command `git cherry-pick` is used to apply the changes done in
one  commit on a given  repository, to  a clean  working tree (no
modifications from the HEAD commit). This is particularly interesting
to a FoI repo, where you can commit mistakes, or unwanted changes, and 
re-commit your work without disturbing shared work.

		git cherry-pick hash

Option `-x` appends a line indicating the original commit that points to.
`git help cherry-pick`: 
	'Do not use this option if you are cherry-picking from your private
branch' -FoI in this case. Well, this is a special 'branch',
it's a repository that sources files from any given repository,
but it is not a canonical branch of any, it is a File of Interest: a bunch
of files, that for some reason, they have any interest to remark by itself.

Suppose you are working on a temporal branch -to fix some issue, test 
some code or similar job. Now you commit your work to get a clean
working tree. The next step is to return to the _master_ branch and
continue working with what you were doing before. 

As stated lines above, the _temporal nature_ of the branch, is suitable
to be erased as soon as you think the issue was solved and the branch
is not needed anymore. Here is where appears the problem, because using
the `-x` flag it will mark the commit you picked-up, pointing to nothing, 
since the branch has been removed. A similar situation pops-up when
the branch is just local; no one can read the _commit from_ in your 
local repository.

Repos like this, can be used as index. It's not a repo that anyone will
erase; a branch in a development scenario could continue or not.
This repository is a kind of place where the owner can drop files of
interest. 

It's sustainable without any file; the logs are always there. Git knowledge
spokes about this as "git history". Wonderful, 

This convention conflicts with lines above, a banned degree and others
trains of; can appear from a user perspective. Several ways to avoid
this conflicts are known on replicating commands as `rpm -q pkg`; a
trivial example to query in some way, _what_ and _what not,_ can be do it.





__Warning:__ with file backups, this technique of hard-linking files
is a process silently dangerous, you should not link any file.bak
or the state of the file will change without notice.


### 4. Bitacora files
### 5. LICENSE files
### 6. README files
### 7. Git ignores


