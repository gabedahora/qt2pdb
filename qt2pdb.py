def pdbqt_to_pdb(pdbqt_file, pdb_file):
    with open(pdbqt_file, 'r') as infile, open(pdb_file, 'w') as outfile:
        for line in infile:
            if line.startswith('MODEL') or line.startswith('ATOM') or line.startswith('HETATM'):
                outfile.write(line)
            elif line.startswith('ENDMDL'):
                outfile.write('END\n')
    print(f"Converted {pdbqt_file} to {pdb_file}")

# Call the function with your file paths
pdbqt_to_pdb('all.pdbqt', 'output_all.pdb')
