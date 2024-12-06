#!/bin/python
import glob
import re

def extract_lowest_binding_energy(file_path):
  """Extracts the lowest binding energy from a Vina output file.

  Args:
    file_path: /media/…/allpubchem million by million/active mols/sdf_files/result

  Returns:
    The lowest binding energy as a float.
  """

  with open(file_path, 'r') as f:
    for line in f:
      match = re.search(r"REMARK VINA RESULT: \s*(-?\d+\.\d+)", line)
      if match:
        return float(match.group(1))
  return None

def main():
  output_file = "lowest_energies.txt"
  with open(output_file, 'w') as out_file:
    for file_path in glob.glob('*out_'):
      lowest_energy = extract_lowest_binding_energy(file_path)
      if lowest_energy is not None:
        out_file.write(f"{file_path}\t{lowest_energy}\n")

if __name__ == "__main__":
  main()
