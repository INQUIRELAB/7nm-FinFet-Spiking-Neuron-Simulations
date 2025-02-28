v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 293.75 -168.75 368.75 -168.75 {
lab=vdd!}
N 206.25 -168.75 293.75 -168.75 {
lab=vdd!}
N 148.75 -168.75 206.25 -168.75 {
lab=vdd!}
N 86.25 -138.75 118.75 -138.75 {
lab=#net1}
N 86.25 -138.75 86.25 -136.25 {
lab=#net1}
N 102.5 -138.75 102.5 -106.25 {
lab=#net1}
N 150 -106.25 150 -90 {
lab=#net2}
N 148.75 -106.25 150 -106.25 {
lab=#net2}
N 263.75 -138.75 263.75 -48.75 {
lab=#net2}
N 150 -98.75 206.25 -98.75 {
lab=#net2}
N 206.25 -98.75 263.75 -98.75 {
lab=#net2}
N 293.75 -106.25 293.75 -78.75 {
lab=#net3}
N 368.75 -105 368.75 -77.5 {
lab=#net4}
N 338.75 -138.75 338.75 -48.75 {
lab=#net3}
N 293.75 -92.5 337.5 -92.5 {
lab=#net3}
N 337.5 -92.5 338.75 -92.5 {
lab=#net3}
N 327.5 -192.5 327.5 -92.5 {
lab=#net3}
N 236.25 -193.75 327.5 -192.5 {
lab=#net3}
N 371.25 -168.75 371.25 -153.75 {
lab=vdd!}
N 368.75 -168.75 371.25 -168.75 {
lab=vdd!}
N 296.25 -168.75 296.25 -153.75 {
lab=vdd!}
N 151.25 -168.75 151.25 -153.75 {
lab=vdd!}
N 250 -51.25 250 -30 {
lab=#net4}
N 236.25 -51.25 250 -51.25 {
lab=#net4}
N 170 -190 170 -168.75 {
lab=vdd!}
N 185 -20 185 42.5 {
lab=gnd!}
N 185 -21.25 185 -20 {
lab=gnd!}
N 185 -21.25 206.25 -21.25 {
lab=gnd!}
N 185 -28.75 185 -21.25 {
lab=gnd!}
N 295 -16.25 295 31.25 {
lab=gnd!}
N 293.75 -16.25 295 -16.25 {
lab=gnd!}
N 295 -16.25 368.75 -16.25 {
lab=gnd!}
N 371.25 -33.75 371.25 -16.25 {
lab=gnd!}
N 368.75 -16.25 371.25 -16.25 {
lab=gnd!}
N 296.25 -33.75 296.25 -16.25 {
lab=gnd!}
N 368.75 -93.75 393.75 -93.75 {
lab=#net4}
N 393.75 -93.75 393.75 -2.5 {
lab=#net4}
N 276.25 -2.5 393.75 -2.5 {
lab=#net4}
N 256.25 -42.5 276.25 -2.5 {
lab=#net4}
N 250 -42.5 256.25 -42.5 {
lab=#net4}
N 55 -90 56.25 -90 {
lab=#net1}
N 56.25 -168.75 148.75 -168.75 {
lab=vdd!}
N 56.25 -168.75 56.25 -166.25 {
lab=vdd!}
N 53.75 -166.25 56.25 -166.25 {
lab=vdd!}
N 53.75 -166.25 53.75 -151.25 {
lab=vdd!}
N 55 -103.75 55 -90 {
lab=#net1}
N 55 -103.75 56.25 -103.75 {
lab=#net1}
N 56.25 -103.75 102.5 -103.75 {
lab=#net1}
N 102.5 -106.25 102.5 -103.75 {
lab=#net1}
N 236.25 -193.75 236.25 -138.75 {
lab=#net3}
N 203.75 -168.75 203.75 -153.75 {
lab=vdd!}
N 206.25 -22.5 206.25 -21.25 {
lab=gnd!}
N 203.75 -40 203.75 -21.25 {
lab=gnd!}
N 236.25 -55 236.25 -51.25 {
lab=#net4}
N 206.25 -106.25 206.25 -85 {
lab=#net2}
N 150 -30 185 -28.75 {
lab=gnd!}
N 55 -30 150 -30 {
lab=gnd!}
N 250 30 295 31.25 {
lab=gnd!}
N 185 30 250 30 {
lab=gnd!}
N 368.75 -106.25 368.75 -105 {
lab=#net4}
C {FinFet Technology/PFFet7.sym} 45 -145 0 0 {name=Npmos2 model=BSIMCMG_osdi_P nfin=\{NFFins\}}
C {FinFet Technology/PFFet7.sym} 190 -145 0 0 {name=Npmos5 model=BSIMCMG_osdi_P nfin=\{NFFins\}}
C {FinFet Technology/PFFet7.sym} 265 -145 0 0 {name=Npmos7 model=BSIMCMG_osdi_P nfin=\{NFFins\}}
C {FinFet Technology/NFFet7.sym} 190 -55 0 0 {name=Nnmos6 model=BSIMCMG_osdi_N nfin=\{NFNFins\}}
C {FinFet Technology/NFFet7.sym} 265 -55 0 0 {name=Nnmos8 model=BSIMCMG_osdi_N nfin=\{NFNFins\}}
C {devices/capa.sym} 250 0 0 0 {name=C2
m=1
value=50f
footprint=1206
device="ceramic capacitor"}
C {devices/capa.sym} 150 -60 0 0 {name=C1
m=1
value=50f
footprint=1206
device="ceramic capacitor"}
C {devices/vdd.sym} 170 -190 0 0 {name=l1 lab=vdd!}
C {devices/gnd.sym} 185 40 0 0 {name=l2 lab=gnd!}
C {devices/simulator_commands_shown.sym} 431.25 -413.75 0 0 {name=COMMANDS
simulator=ngspice
only_toplevel=false 
value="
* ngspice commands
.include asap7_TT_slvt.sp
.param NFFins=1
.param NFNFins=5
Vvdd vdd! 0 dc=0.7
Vgnd gnd! 0 dc=0
.ic v(net2)=0 v(net4)=0
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
    
    echo VDD Cap1 Cap2 Spikes Frequency Energy_Per_Spike > /Users/logan/Desktop/besourneuron.txt
    
    alter Isyn = 100n 
    
    foreach vdd 0.1 0.11 0.12 0.13 0.14 0.15 0.16 0.17 0.18 0.19 0.2 0.21 0.22 0.23 0.24 0.25 0.26 0.27 0.28 0.29 0.3 0.31 0.32 0.33 0.34 0.35 0.36 0.37 0.38 0.39 0.4 0.41 0.42 0.43 0.44 0.45 0.46 0.47 0.48 0.49 0.5 0.51 0.52 0.53 0.54 0.55 0.56 0.57 0.58 0.59 0.6 0.61 0.62 0.63 0.64 0.65 0.66 0.67 0.68 0.69 0.7 0.71 0.72 0.73 0.74 0.75 0.76 0.77 0.78 0.79 0.8 0.81 0.82 0.83 0.84 0.85 0.86 0.87 0.88 0.89 0.9
        alter Vvdd dc=$vdd
        let vth = 0.2 * $vdd
        let low_th = 0.05 * $vdd
        
        foreach cap1 0.1e-15 0.2e-15 0.3e-15 0.4e-15 0.5e-15 0.6e-15 0.7e-15 0.8e-15 0.9e-15 1e-15 2e-15 3e-15 4e-15 5e-15 6e-15 7e-15 8e-15 9e-15 10e-15
            alter C1 = $cap1
            
            foreach cap2 0.1e-15 0.2e-15 0.3e-15 0.4e-15 0.5e-15 0.6e-15 0.7e-15 0.8e-15 0.9e-15 1e-15 2e-15 3e-15 4e-15 5e-15 6e-15 7e-15 8e-15 9e-15 10e-15
                alter C2 = $cap2
                
                tran 0.04n 20n UIC
                
                let power_vdd = -1*v(vdd!)*i(Vvdd)
                let dt = time[1] - time[0]
                
                let transitions = vector(length(v(net4)))
                let i = 0
                let count = 0
                let last_state = 0
                let spike_energy = 0
                let current_spike_energy = 0
                
                dowhile i < length(v(net4))-1
                    if (v(net4)[i] gt $&vth and last_state eq 0)
                        let count = count + 1
                        let last_state = 1
                        let current_spike_energy = 0
                    end
                    if (last_state eq 1)
                        let current_spike_energy = current_spike_energy + power_vdd[i] * $&dt
                    end
                    if (v(net4)[i] lt $&low_th)
                        if (last_state eq 1)
                            let spike_energy = spike_energy + current_spike_energy
                        end
                        let last_state = 0
                    end
                    let i = i + 1
                end
               
                let spike_count = $&count
                let sim_time = 20e-9
                let spiking_freq = $&spike_count / sim_time
                let energy_per_spike = 0
                if spike_count gt 0
                    let energy_per_spike = (spike_energy / spike_count)
                end
                
                echo $vdd $cap1 $cap2 $&spike_count $&spiking_freq $&energy_per_spike >> /Users/logan/Desktop/besourneuron.txt
                echo At VDD=$vdd V Cap1=$cap1 F Cap2=$cap2 F Spikes=$&spike_count Spikes Freq=$&spiking_freq Hz Energy/Spike=$&energy_per_spike J
            end
        end
    end    
.endc
"

}
C {FinFet Technology/PFFet7.sym} 160 -142.5 0 1 {name=Npmos1 model=BSIMCMG_osdi_P nfin=\{NFFins\}}
C {FinFet Technology/PFFet7.sym} 310 -145 0 1 {name=Npmos3 model=BSIMCMG_osdi_P nfin=\{NFFins\}}
C {FinFet Technology/NFFet7.sym} 310 -61.25 0 1 {name=Nnmos4 model=BSIMCMG_osdi_N nfin=\{NFNFins\}}
C {devices/isource.sym} 55 -60 0 0 {name=Isyn value=101n
}
