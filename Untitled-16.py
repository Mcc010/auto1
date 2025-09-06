#desarolle un algoritmo que le pida mes y dia del año y nos diga que estacion climatica tendra 
mes= input("ingrese el mes que desea consultar: ").lower()
dia= int(input("ingrese el dia que desea consultar: "))
if (mes==("diciembre") and 21<=dia<=31) or (mes==("enero") and 1<=dia<=31) or (mes==("febrero") and 1<=dia<=28) or (mes==("marzo") and 1<=dia<=20):
    print(f"el dia {dia} del mes {mes} estariamos en invierno")
elif (mes==(f"junio")and 21<=dia<=30) or (mes==("julio") and 1<=dia<=31) or (mes==("agosto") and 1<=dia<=31) or (mes==("septiembre") and 1<=dia<=21):
    print(f"el dia {dia} del mes {mes} estariamos en verano")
elif (mes==("septiembre")and 22<=dia<=30) or (mes==("octubre") and 1<=dia<=31) or (mes==("noviembre") and 1<=dia<=30) or (mes==("diciembre") and 1<=dia<=20):
    print(f"el dia {dia} del mes {mes} estariamos en otoño")
elif (mes==("marzo") and 21<=dia<=31) or (mes==("abril") and 1<=dia<=30) or (mes==("mayo") and 1<=dia<=31) or (mes==("junio") and 1<=dia<=20):
    print(f"el dia {dia} del mes {mes} estariamos en otoño")
else:
    print("el mes o dia ingresado son incorrectos")

#21 de diciembre – 20 de marzo invierno
#20 de junio – 21 de septiembre verano
#22 septiembre – 21 dic otoño
#21 de marzo - 21 de junio primavera