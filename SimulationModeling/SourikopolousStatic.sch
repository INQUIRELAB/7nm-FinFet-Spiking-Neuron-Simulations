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
    set num_threads = 8
    set parallel = 1
    set filetype=ascii
    set wr_vecnames
    set wr_singlescale
    
    echo VDD Static_Power > /Users/logan/Desktop/sourikopolousneuron.txt
    
    alter Isyn = 0
    
    alter C1 = 1e-15
    alter C2 = 1e-15
    
    foreach vdd 0.1 0.11 0.12 0.13 0.14 0.15 0.16 0.17 0.18 0.19 0.2 0.21 0.22 0.23 0.24 0.25 0.26 0.27 0.28 0.29 0.3 0.31 0.32 0.33 0.34 0.35 0.36 0.37 0.38 0.39 0.4 0.41 0.42 0.43 0.44 0.45 0.46 0.47 0.48 0.49 0.5 0.51 0.52 0.53 0.54 0.55 0.56 0.57 0.58 0.59 0.6 0.61 0.62 0.63 0.64 0.65 0.66 0.67 0.68 0.69 0.7 0.71 0.72 0.73 0.74 0.75 0.76 0.77 0.78 0.79 0.8 0.81 0.82 0.83 0.84 0.85 0.86 0.87 0.88 0.89 0.9
        alter Vvdd dc=$vdd
        
        tran 0.04n 20n UIC
        
        let power_vdd = -1*v(vdd!)*i(Vvdd)
        let n_points = length(power_vdd)
        let start_idx = n_points - floor(n_points/5)
        
        let i = $&start_idx
        let sum_power = 0
        
        dowhile i < n_points
            let sum_power = sum_power + power_vdd[i]
            let i = i + 1
        end
        
        let static_power = sum_power / (n_points - $&start_idx)
        
        echo $vdd $&static_power >> /Users/logan/Desktop/sourikopolousneuron.txt
        echo At VDD=$vdd V Static_Power=$&static_power W
    end    
.endc
"

}
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
