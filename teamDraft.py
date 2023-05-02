import sample, sys, os
from simAnneal import simAnneal

def main(argv):
    if len(argv) > 1:
        data_file = "data/" + argv[1]
    else:
        data_file = "data/h.matrix.p"

    if not os.path.exists(data_file):
        raise Exception("{} does not exist.".format(data_file))

    data, matrix = sample.main(data_file)

    simAnneal(data, matrix)

if __name__ == "__main__":
    main(sys.argv)
