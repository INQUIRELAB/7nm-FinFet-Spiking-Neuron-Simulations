v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 112.5 -176.25 112.5 -160 {
lab=vdd!}
N 112.5 -160 200 -123.75 {
lab=vdd!}
N 200 -123.75 285 -123.75 {
lab=vdd!}
N 211.25 -123.75 211.25 -108.75 {
lab=vdd!}
N 287.5 -123.75 287.5 -108.75 {
lab=vdd!}
N 285 -123.75 287.5 -123.75 {
lab=vdd!}
N 178.75 -93.75 178.75 -13.75 {
lab=#net1}
N 112.5 -100 112.5 -63.75 {
lab=#net1}
N 112.5 -63.75 178.75 -63.75 {
lab=#net1}
N 151.25 -173.75 215 -173.75 {
lab=#net1}
N 151.25 -173.75 151.25 -63.75 {
lab=#net1}
N 122.5 -63.75 122.5 17.5 {
lab=#net1}
N 255 -93.75 255 -13.75 {
lab=#net2}
N 208.75 -61.25 208.75 -43.75 {
lab=#net2}
N 208.75 -52.5 255 -52.5 {
lab=#net2}
N 285 -61.25 285 -43.75 {
lab=#net3}
N 122.5 80 216.25 80 {
lab=gnd!}
N 216.25 80 216.25 95 {
lab=gnd!}
N 208.75 18.75 286.25 18.75 {
lab=gnd!}
N 208.75 18.75 208.75 80 {
lab=gnd!}
N 120 62.5 120 80 {
lab=gnd!}
N 120 80 122.5 80 {
lab=gnd!}
N 211.25 1.25 211.25 18.75 {
lab=gnd!}
N 287.5 1.25 287.5 18.75 {
lab=gnd!}
N 286.25 18.75 287.5 18.75 {
lab=gnd!}
N 152.5 47.5 313.75 47.5 {
lab=#net3}
N 313.75 -50 313.75 47.5 {
lab=#net3}
N 285 -50 313.75 -50 {
lab=#net3}
N 313.75 -172.5 313.75 -50 {
lab=#net3}
N 313.75 -173.75 313.75 -172.5 {
lab=#net3}
N 276.25 -173.75 313.75 -173.75 {
lab=#net3}
N 215 -173.75 216.25 -173.75 {
lab=#net1}
C {devices/simulator_commands_shown.sym} 411.25 -293.75 0 0 {name=COMMANDS
simulator=ngspice
only_toplevel=false 
value="
* ngspice commands
.include asap7_TT_slvt.sp
.param NFFins=1
.param NFNFins=5
Vvdd vdd! 0 dc=0.7
Vgnd gnd! 0 dc=0
.ic v(net1)=0
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
    
    echo VDD Static_Power > /Users/logan/Desktop/dannevilleneuron.txt
    
    alter Isyn = 0
    
    alter C1 = 0.125e-15
    
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
        
        echo $vdd $&static_power >> /Users/logan/Desktop/dannevilleneuron.txt
        echo At VDD=$vdd V Static_Power=$&static_power W
    end    
.endc
"

}
C {devices/gnd.sym} 216.25 93.75 0 0 {name=l2 lab=gnd!}
C {devices/isource.sym} 112.5 -130 0 0 {name=Isyn value=101n
}
C {devices/vdd.sym} 112.5 -176.25 0 0 {name=l1 lab=vdd!}
C {FinFet Technology/PFFet7.sym} 105 -100 0 0 {name=Npmos1 model=BSIMCMG_osdi_P nfin=\{NFFins\}}
C {FinFet Technology/NFFet7.sym} 105 -20 0 0 {name=Nnmos4 model=BSIMCMG_osdi_N nfin=\{NFNFins\}}
C {FinFet Technology/PFFet7.sym} 181.25 -100 0 0 {name=Npmos2 model=BSIMCMG_osdi_P nfin=\{NFFins\}}
C {FinFet Technology/NFFet7.sym} 181.25 -20 0 0 {name=Nnmos1 model=BSIMCMG_osdi_N nfin=\{NFNFins\}}
C {devices/capa.sym} 246.25 -173.75 3 0 {name=C1
m=1
value=50f
footprint=1206
device="ceramic capacitor"}
C {FinFet Technology/NFFet7.sym} 226.25 41.25 0 1 {name=Nnmos2 model=BSIMCMG_osdi_N nfin=\{NFNFins\}}
