from pycirculate.anova import AnovaController
import datetime

ANOVA_MAC_ADDRESS = "10:CE:A9:CB:D2:FA"
TEMP = 42.0

def main():
    ctrl = AnovaController(ANOVA_MAC_ADDRESS)
    print(datetime.datetime.now())
    print(ctrl.read_temp(), ctrl.read_unit())
    print(ctrl.set_temp(TEMP))
    #print(ctrl.start_anova())
    print(ctrl.anova_status())

if __name__ == "__main__":
    main()
