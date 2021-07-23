from os import path, system
from shutil import copyfile
from pdbtools import PDB

class AtomnameAgent:

    def __init__(self, pdb_in, pdb_out, resname_map, atomname_map):
        self.pdb_in = pdb_in
        self.pdb_out = pdb_out

        self.resname_map = resname_map
        self.atomname_map = atomname_map

        self.temp_pdb = path.join('.', 'temp.pdb')

    def check_pdbin_header_footer(self):
        print('Check skip_header and skip_footer by ...')
        print(f'vim {self.pdb_in}')

    def convert_resname_atomname(self, skip_header, skip_footer):
        copyfile(self.pdb_in, self.temp_pdb)
        print(f'cp {self.pdb_in} {self.temp_pdb}')

        reader = PDB.PDBReader(self.temp_pdb, skip_header=skip_header, skip_footer=skip_footer)

        for atom in reader.atomgroup:
            old_resname = atom.resname
            new_resname = self.resname_map[old_resname]
            atom.set_resname(new_resname)

            old_atomname = atom.name
            new_atomname = self.atomname_map[old_resname][old_atomname]
            atom.set_atomname(new_atomname)

        writer = PDB.PDBWriter(self.pdb_out, reader.atomgroup)
        writer.write_pdb()
        print(f'Reset {self.pdb_out}!')
        print(f'Check by...\nvim {self.pdb_out}')

        cmd = f'rm {self.temp_pdb}'
        system(cmd)
        print(cmd)
