print("Co chcesz obliczyć")
print("a) siła wyporu")
print("b) gęstość cieczy")
print("c) gęstość ciała")
print("d) objętość wypartej cieczy")
print("e) objętość ciała")
print("Twój wybór:")
opcja = input()
if opcja in ("a", "A"):
    print("Podaj gęstość cieczy(m3/kg)")
    dc = float(input())
    print("Podaj objętość wypartej cieczy(m3)")
    Vw = float(input())
    print("Fw = dc * Vw * g = ", dc * Vw * 10, "N")
elif opcja in ("b", "B"):
    print("Podaj gęstość ciała(m3/kg)")
    dci = float(input())
    print("Podaj objętość ciała(m3)")
    Vc = float(input())
    print("Podaj objętość wypartej cieczy(m3)")
    Vw = float(input())
    print("dc = dci * Vc / Vw = ", dci * Vc / Vw, "m3/kg")
elif opcja in ("c", "C"):
    print("Podaj gęstość ciecz(m3/kg)")
    dc = float(input())
    print("Podaj objętość wypartej cieczy(m3)")
    Vw = float(input())
    print("Podaj objętość ciała stałego(m3)")
    Vc = float(input())
    print("dci = dc * Vw / Vc = ", dc * Vw / Vc, "m3/kg")
elif opcja in ("d", "D"):
    print("Podaj gęstość ciała(m3/kg)")
    dci = float(input())
    print("Podaj objętość ciała(m3)")
    Vc = float(input())
    print("Podaj gęstość cieczy(m3/kg)")
    dc = float(input())
    print("Vw = dci * Vc / dc = ", dci * Vc / dc, "kg")
elif opcja in ("e", "E"):
    print("Podaj gęstość cieczy(m3/kg)")
    dc = float(input())
    print("Podaj objętość wypartej cieczy(m3)")
    Vw = float(input())
    print("Podaj gęstość ciała(m3/kg)")
    dci = float(input())
    print("Vc = dc * Vw / dci = ", dc * Vw / dci, "kg")
elif opcja == "fizyka":
    print("\033[1;31;40m Player fell victim of gravity  \n")
else:
    print("\033[1;31;40m !!!ERROR!!!  \n")
    print("\033[1;31;40m Musisz podać jedną z powyszych liter  \n")
