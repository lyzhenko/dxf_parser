import ezdxf

dxf = ezdxf.readfile('data/f.dxf')

model = dxf.modelspace()
for e in model:
    if e.dxf.dxftype == 'LINE':
        print(e.dxf.layers)



print()