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
some interest to remark by itself.

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
### Spec files
### Bitacora files
### LICENSE files
### README files
### Git ignores


