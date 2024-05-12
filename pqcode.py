import pyqrcode

from pyqrcode import QRCode
  #on recupere le   lien
  #on prend pour exemple le lien de google
  s= "https://www.google.com"


  #génére le code QR
 url = pyqrcode.create(s)
  #creation et sauvegarde du fichier contenant le code
 url.svg("togoogle.ml", scale=8)


