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
C {devices/simulator_commands_shown.sym} 451.25 -443.75 0 0 {name=COMMANDS
simulator=ngspice
only_toplevel=false 
value="
* ngspice commands
.include asap7_TT_slvt.sp
.param NFFins=1
.param NFNFins=5
* Power supplies
Vvdd vdd! 0 dc=0.7
Vgnd gnd! 0 dc=0
* Initial conditions
.ic v(net2)=0 v(net4)=0
.control
    * Reduce maximum timestep
    set maxstep = 0.01n
    
    * Add integration method controls
    set method = gear
    set gmin = 1e-15
    
    * Increase iteration limits
    set itl1 = 1000
    set itl4 = 1000
    set num_threads = 24
    set parallel = 1
    set filetype=ascii
    set wr_vecnames
    set wr_singlescale
    
    * Create output file in current directory
    echo VDD Cap1 Cap2 Spikes Frequency Energy_Per_Spike > /Users/logan/Desktop/besourneuron.txt
    
    alter Isyn = 100n 
    
    let vdd_start = 0.1
    let vdd_stop = 0.91
    let vdd_step = 0.01
    let vdd = $&vdd_start
    
    while vdd <= $&vdd_stop
        alter Vvdd dc=$&vdd
        let vth = 0.2 * $&vdd
        let low_th = 0.05 * $&vdd
        
        foreach cap1 0.69e-15
            alter C1 = $cap1
            
            foreach cap2 0.2e-15
                alter C2 = $cap2
                
                tran 0.04n 1u UIC
                
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
                let sim_time = 1e-6
                let spiking_freq = $&spike_count / sim_time
                let energy_per_spike = 0
                if spike_count gt 0
                    let energy_per_spike = (spike_energy / spike_count)
                end
                
                * Write to file and also echo to screen
                echo $&vdd $cap1 $cap2 $&spike_count $&spiking_freq $&energy_per_spike >> /Users/logan/Desktop/besourneuron.txt
                echo At VDD=$&vdd V Cap1=$cap1 F Cap2=$cap2 F Spikes=$&spike_count Spikes Freq=$&spiking_freq Hz Energy/Spike=$&energy_per_spike J
            end
        end
        let vdd = vdd + $&vdd_step
    end    
.endc
"


}
C {FinFet Technology/PFFet7.sym} 160 -142.5 0 1 {name=Npmos1 model=BSIMCMG_osdi_P nfin=\{NFFins\}}
C {FinFet Technology/PFFet7.sym} 310 -145 0 1 {name=Npmos3 model=BSIMCMG_osdi_P nfin=\{NFFins\}}
C {FinFet Technology/NFFet7.sym} 310 -61.25 0 1 {name=Nnmos4 model=BSIMCMG_osdi_N nfin=\{NFNFins\}}
C {devices/isource.sym} 55 -60 0 0 {name=Isyn value=101n
}
