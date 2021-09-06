## Hieronder een verzameling van kleuren
# b: blauw         # m: magenta      # c: cyaan
# g: groen         # y: geel         # w: wit
# r: rood          # k: zwart

## Het is ook mogelijk om de stijl te varieren. Enkele voorbeelden zijn:
#--: gestreepte lijn                 # .: punten
# o:  grote punten                   # -:  lijn

## Alle opties kunnen aan plt.plot() worden toegevoegd.
## Het voorbeeld hieronder produceert een plaatje met lijn en punten.
x = np.linspace(0,2*np.pi)

plt.figure()                # nieuwe figuur
plt.plot(x,np.cos(x),'r-')  # cosinus plotten
plt.plot(x,np.cos(x),'k.')  # nog een cosinus eroverheen plotten
plt.show()                  # forceer om weer te geven