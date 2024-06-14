from FigureReader import FigureReader
pust=[]
pusty=[]
if __name__ == "__main__":
    for file in ['input03.txt']:
        reader = FigureReader(file)
        figures = reader.read()
        for figure in figures:

            print(figure, "Dimension =", figure.dimension(), "Perimeter =", figure.perimeter(), "Square =", figure.square(), "SquareSurface =", figure.squareSurface(), "SquareBase =", figure.squareBase(), "Height =", figure.height(), "Volume =", figure.volume(), )

        for figure in figures:
            bonk=figure.volume()
            pust.append(bonk)
            try:
                bam=figure.volume()
                pusty.append(bam)
            except AttributeError:
                pass
        maxAttributes = [0]
        maxFigure = figures[0]
        for figure in figures:
            try:
                if figure.volume() > maxAttributes[0]:
                    maxAttributes = [figure.volume()]
                    maxFigure = figure
            except TypeError:
                continue
        for i in pust:
            try:
                pust.remove(None)
            except ValueError:
                break
        print("The biggest volume has", maxFigure, "It's volume =", (max(pust)))
