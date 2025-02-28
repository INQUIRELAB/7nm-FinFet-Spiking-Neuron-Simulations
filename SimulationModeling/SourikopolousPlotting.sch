v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 113.75 -131.25 113.75 -92.5 {
lab=#net1}
N 143.75 -163.75 143.75 -62.5 {
lab=#net2}
N 193.75 -131.25 193.75 -92.5 {
lab=#net2}
N 143.75 -111.25 193.75 -111.25 {
lab=#net2}
N 223.75 -163.75 223.75 -62.5 {
lab=#net3}
N 293.75 -130 293.75 -91.25 {
lab=#net3}
N 223.75 -111.25 293.75 -111.25 {
lab=#net3}
N 293.75 -111.25 357.5 -111.25 {
lab=#net3}
N 357.5 -128.75 357.5 -111.25 {
lab=#net3}
N 357.5 -111.25 357.5 -87.5 {
lab=#net3}
N 113.75 -193.75 293.75 -193.75 {
lab=vdd!}
N 240 -222.5 240 -193.75 {
lab=vdd!}
N 240 -222.5 357.5 -222.5 {
lab=vdd!}
N 357.5 -222.5 357.5 -190 {
lab=vdd!}
N 111.25 -193.75 113.75 -193.75 {
lab=vdd!}
N 111.25 -193.75 111.25 -178.75 {
lab=vdd!}
N 191.25 -193.75 191.25 -178.75 {
lab=vdd!}
N 296.25 -193.75 296.25 -178.75 {
lab=vdd!}
N 293.75 -193.75 296.25 -193.75 {
lab=vdd!}
N 247.5 -61.25 247.5 -42.5 {
lab=#net1}
N 247.5 -61.25 263.75 -61.25 {
lab=#net1}
N 113.75 -30 193.75 -30 {
lab=gnd!}
N 170 -28.75 170 40 {
lab=gnd!}
N 170 -30 170 -28.75 {
lab=gnd!}
N 111.25 -30 113.75 -30 {
lab=gnd!}
N 111.25 -47.5 111.25 -30 {
lab=gnd!}
N 191.25 -47.5 191.25 -30 {
lab=gnd!}
N 170 17.5 247.5 17.5 {
lab=gnd!}
N 246.25 18.75 290 18.75 {
lab=gnd!}
N 290 -28.75 290 18.75 {
lab=gnd!}
N 290 -28.75 357.5 -28.75 {
lab=gnd!}
N 296.25 -46.25 296.25 -28.75 {
lab=gnd!}
N 357.5 -28.75 357.5 -26.25 {
lab=gnd!}
N 186.25 -3.75 247.5 -61.25 {
lab=#net1}
N 91.25 -3.75 186.25 -3.75 {
lab=#net1}
N 91.25 -113.75 91.25 -3.75 {
lab=#net1}
N 91.25 -113.75 112.5 -113.75 {
lab=#net1}
N 112.5 -113.75 113.75 -113.75 {
lab=#net1}
N 205 -212.5 263.75 -163.75 {
lab=#net2}
N 170 -212.5 205 -212.5 {
lab=#net2}
N 170 -212.5 170 -111.25 {
lab=#net2}
N 247.5 17.5 247.5 18.75 {
lab=gnd!}
N 357.5 -130 357.5 -128.75 {
lab=#net3}
N 293.75 -131.25 293.75 -130 {
lab=#net3}
C {devices/simulator_commands_shown.sym} 401.25 -293.75 0 0 {name=COMMANDS
simulator=ngspice
only_toplevel=false 
value="
* ngspice commands
.include asap7_TT_slvt.sp
.param NFFins=1
.param NFNFins=5
Vvdd vdd! 0 dc=0.7
Vgnd gnd! 0 dc=0
.ic v(net1)=0 v(net3)=0
.control
    set maxstep = 0.01n
    
    set method = gear
    set gmin = 1e-15
    
    set itl1 = 1000
    set itl4 = 1000
    set num_threads = 24
    set parallel = 1
    set filetype=ascii
    set wr_vecnames
    set wr_singlescale
    
    alter Isyn = 100n
    
    alter C1 = 1e-15
    alter C2 = 1e-15
    
    foreach vdd 0.4
        alter Vvdd dc=$vdd
        
        tran 0.04n 30n UIC
        
        wrdata /Users/logan/Desktop/net1_data.txt time v(net1)
        wrdata /Users/logan/Desktop/net3_data.txt time v(net3)
        
        plot v(net1)
        plot v(net3)
    end    
.endc
"}
C {FinFet Technology/PFFet7.sym} 217.5 -170 0 1 {name=Npmos3 model=BSIMCMG_osdi_P nfin=\{NFFins\}}
C {FinFet Technology/NFFet7.sym} 217.5 -68.75 0 1 {name=Nnmos1 model=BSIMCMG_osdi_N nfin=\{NFNFins\}}
C {FinFet Technology/PFFet7.sym} 297.5 -170 0 1 {name=Npmos4 model=BSIMCMG_osdi_P nfin=\{NFFins\}}
C {FinFet Technology/NFFet7.sym} 297.5 -68.75 0 1 {name=Nnmos2 model=BSIMCMG_osdi_N nfin=\{NFNFins\}}
C {FinFet Technology/PFFet7.sym} 190 -170 0 0 {name=Npmos5 model=BSIMCMG_osdi_P nfin=\{NFFins\}}
C {FinFet Technology/NFFet7.sym} 190 -67.5 0 0 {name=Nnmos3 model=BSIMCMG_osdi_N nfin=\{NFNFins\}}
C {devices/isource.sym} 357.5 -160 0 0 {name=Isyn value=101n
}
C {devices/capa.sym} 247.5 -12.5 0 0 {name=C2
m=1
value=50f
footprint=1206
device="ceramic capacitor"}
C {devices/capa.sym} 357.5 -57.5 0 0 {name=C1
m=1
value=50f
footprint=1206
device="ceramic capacitor"}
C {devices/vdd.sym} 240 -222.5 0 0 {name=l1 lab=vdd!}
C {devices/gnd.sym} 170 40 0 0 {name=l2 lab=gnd!}
