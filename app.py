import ezdxf

dxf = ezdxf.readfile('f.dxf')

model = dxf.modelspace()
for e in model:
    if e.dxf.dxftype == 'LINE':
        print(e.dxf.layers)

#lines = [e for e in dxf.entities if e.dxftype == 'LINE']

print()