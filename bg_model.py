import matplotlib
from netpyne import specs, sim 
from neuron import h
import os

%matplotlib inline

os.chdir(r"C:\Users\Maria\Desktop\PhD\Code\NetPyNE_course\model")

!nrnivmodl

#%% Network parameters
netParams = specs.NetParams()  # object of class NetParams to store the network parameters

#%% Create cells

# Initialize ion concentrations
h("cai0_ca_ion = 5e-6 ")
h("cao0_ca_ion = 2")
h("ki0_k_ion = 105") 
h("ko0_k_ion = 3")
h("nao0_na_ion = 108")
h("nai0_na_ion = 10")

netParams.cellParams['GPe'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {
                "nseg": 1,
                "diam": 60,
                "L": 60,
                "Ra": 200.0,
                "cm": 1
            },
            "mechs": {
                'myions': {},
                "GPeA": {
                    "gnabar": 0.04,
                    "gkdrbar": 0.0042,
                    "gkcabar": 0.1e-3, 
                    "gcatbar": 6.7e-5, 
                    "kca": 2, 
                    "gl": 4e-5
                }
            }
        }
    }
}

netParams.cellParams['STN'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {
                "nseg": 1,
                "diam": 60,
                "L": 60,
                "Ra": 200.0,
                "cm": 1
            },
            "mechs": {
                'myions': {},
                "stn": {
                    "gnabar": 49e-3,
                    "gkdrbar": 57e-3,
                    "gkabar": 5e-3, 
                    "gkcabar": 1.0e-3, 
                    "gcalbar": 15e-3,
					"gcatbar": 5e-3, 
                    "kca": 2, 
                    "gl": 0.35e-3
                }
            }
        }
    }
}

netParams.cellParams['Th'] = {
    "conds": {},
    "secs": {
        "soma": {
            'threshold': -10,
            "geom": {
                "nseg": 1,
                "diam": 100,
                "L": 100,
                "Ra": 150.0,
                "cm": 100
            },
            "mechs": {
                'thalamic_i_leak': {},
                "thalamic_i_na_k": {},
                "thalamic_i_t": {}
            },
            "pointps": {
                'SN': {
                 'mod': 'SynNoise',
                 'f0': 0,
                 'f1': 0.3}
            }
        }
    }
}

netParams.cellParams['Inter'] = {
    "conds": {},
    "secs": {
        "soma": {
            "geom": {
                "nseg": 1,
                "diam": 25,
                "L": 35,
                "Ra": 150.0,
                "cm": 1
            },
            "mechs": {
                'interneuron_i_leak': {},
                "interneuron_i_na": {},
                "interneuron_i_k": {}
            },
            "pointps": {
                'SN': {
                 'mod': 'SynNoise',
                 'f0': 0,
                 'f1': 0.3}
            }
        }
    }
}

## NetStim artificial spike generator
netParams.cellParams['Str'] = {
    'cellModel': 'NetStim'}

#%% cortex cells - can change to any other model
netParams.importCellParams(
    label='pyr',
    conds={'cellType': 'pyr_type', 'cellModel': 'pyr_model'},
    fileName='c91662.CNG.swc', 
    cellName='celldef',
    importSynMechs=False);
    
netParams.renameCellParamsSec('pyr', 'soma_0', 'soma')  # rename imported section 'soma_0' to 'soma'

#netParams.cellParams['pyr']['secs']['soma']['geom']['Ra'] = 150 #if want same Ra everywhere
netParams.cellParams['pyr']['secs']['soma']['mechs']['hh'] = {}
#if want mechanisms like in fleming
# netParams.cellParams['pyr']['secs']['soma']['mechs']['cortical_soma_i_leak'] = {}
# netParams.cellParams['pyr']['secs']['soma']['mechs']['cortical_soma_i_na'] = {}
# netParams.cellParams['pyr']['secs']['soma']['mechs']['cortical_soma_i_k'] = {}
# netParams.cellParams['pyr']['secs']['soma']['mechs']['cortical_soma_i_m'] = {}
netParams.cellParams['pyr']['secs']['soma']['pointps']['SN'] = {'mod': 'SynNoise', 'f0': 0, 'f1': 0.3}
netParams.cellParams['pyr']['secs']['soma']['threshold'] = -10 #?? tunable

netParams.cellParams['pyr']['secs']['axon_0']['mechs']['hh'] = {}
#netParams.cellParams['pyr']['secs']['axon_0']['geom']['Ra'] = 150 #if want same Ra everywhere
#if want mechanisms like in fleming, tunable
# netParams.cellParams['pyr']['secs']['axon_0']['mechs']['cortical_axon_i_leak'] = {'g_l': 3.3e-5}#0.02}
# netParams.cellParams['pyr']['secs']['axon_0']['mechs']['cortical_axon_i_na'] = {'g_Na': 4000e-4}#2800e-4}
# netParams.cellParams['pyr']['secs']['axon_0']['mechs']['cortical_axon_i_kv'] = {'g_Kv': 20e-4}#5e-4}
# netParams.cellParams['pyr']['secs']['axon_0']['mechs']['cortical_axon_i_kd'] = {'g_Kd': 0.015}#0.0072}

#%% Create population
pop_Size=10

netParams.popParams['GPe_pop'] = {
    "cellModel": "",
    "cellType": 'GPe',
    "numCells": pop_Size,
    "yRange": [
        250,
        750
    ],
    "xRange": [
        0,
        250
    ],
    "zRange": [
        0,
        100
    ]
}

netParams.popParams['GPi_pop'] = {
    "cellModel": "",
    "cellType": 'GPe',
    "numCells": pop_Size,
    "yRange": [
        0,
        500
    ],
    "xRange": [
        250,
        750
    ],
    "zRange": [
        0,
        100
    ]
}

netParams.popParams['STN_pop'] = {
    "cellModel": "",
    "cellType": 'STN',
    "numCells": pop_Size,
    "yRange": [
        0,
        500
    ],
    "xRange": [
        0,
        500
    ],
    "zRange": [
        0,
        100
    ]
}

netParams.popParams['Th_pop'] = {
    "cellModel": "",
    "cellType": 'Th',
    "numCells": pop_Size,
    "yRange": [
        0,
        500
    ],
    "xRange": [
        500,
        1000
    ],
    "zRange": [
        0,
        100
    ]
}

netParams.popParams['Inter_pop'] = {
    "cellModel": "",
    "cellType": 'Inter',
    "numCells": pop_Size
    # "yRange": [
    #     0,
    #     500
    # ],
    # "xRange": [
    #     500,
    #     1000
    # ],
    # "zRange": [
    #     0,
    #     100
    # ]
}

netParams.popParams['Cort_pop'] = {
    "cellModel": "pyr_model",
    "cellType": 'pyr_type',
    "numCells": pop_Size
    # "yRange": [
    #     0,
    #     500
    # ],
    # "xRange": [
    #     500,
    #     1000
    # ],
    # "zRange": [
    #     0,
    #     100
    # ]
}

#check!! - modify upon healthy state
netParams.popParams['Str_pop'] = {
    "cellModel": "",
    "cellType": 'Str',
    'rate': 5,
    'noise': 0, #check if needed
    'start': 1, #check if needed
    "numCells": pop_Size
}

#%% Add stimulus
#check out amplitude again!!
netParams.stimSourceParams['bias_gpe'] = {'type': 'IClamp', 'del': 0, 'dur': 1e12, 'amp':-0.009}# 0.04} #-0.009
netParams.stimSourceParams['bias_gpi'] = {'type': 'IClamp', 'del': 0, 'dur': 1e12, 'amp': 0.006}#0.33} #0.006 #0.356
netParams.stimSourceParams['bias_stn'] = {'type': 'IClamp', 'del': 0, 'dur': 1e12, 'amp': -0.125}#0} #-0.125 #0.6
netParams.stimSourceParams['bias_inter'] = {'type': 'IClamp', 'del': 0, 'dur': 1e12, 'amp': 0.070} 
netParams.stimSourceParams['bias_cort'] = {'type': 'IClamp', 'del': 0, 'dur': 1e12, 'amp': 0.245} 
#no bias current for thalamus in original paper
# netParams.stimSourceParams['bkg']={
#     'type': 'NetStim',
#     'rate': 12,
#     'noise': 0.2
# }

#%% Add target
netParams.stimTargetParams['bias_gpe->gpe'] = {'source': 'bias_gpe','sec':'soma', 'loc': 0.5, 'conds': {'pop':'GPe_pop'}}
netParams.stimTargetParams['bias_gpi->gpi'] = {'source': 'bias_gpi','sec':'soma', 'loc': 0.5, 'conds': {'pop':'GPi_pop'}}
netParams.stimTargetParams['bias_stn->stn'] = {'source': 'bias_stn','sec':'soma', 'loc': 0.5, 'conds': {'pop':'STN_pop'}}
netParams.stimTargetParams['bias_inter->inter'] = {'source': 'bias_inter','sec':'soma', 'loc': 0.5, 'conds': {'pop':'Inter_pop'}}
netParams.stimTargetParams['bias_cort->cort'] = {'source': 'bias_cort', 'sec':'soma', 'loc': 0.5,'conds': {'pop':'Cort_pop'}}

#%% Synaptic mechanism parameters
netParams.synMechParams['AMPA'] = {'mod': 'AMPA_S'}  # excitatory synaptic mechanism
netParams.synMechParams['AMPA_axon'] = {'mod': 'AMPA_S', 'selfNetCon': {'sec': 'axon_0'}}  # excitatory synaptic mechanism
netParams.synMechParams['GABA'] = {'mod': 'GABAa_S'}  # inhibitory synaptic mechanism

# netParams.stimTargetParams['bkg->Th'] = {
#     'source': 'bkg',
#     'conds': {'cellType': 'Th'},
#     'weight': 1,
#     'sec': 'soma',
#     'loc': 0.5,
#     'delay': 5,
#     'synMech': 'GABA'
# }
#%% Connections
netParams.connParams['STN->GPe'] = {
    'preConds': {'pop': 'STN_pop'}, 
    'postConds': {'pop': 'GPe_pop'},
    'weight': 0.111111,
    'convergence': 1,
    'sec': 'soma',
    'loc': 0.5,
    'synMech': 'AMPA',
    'delay': 4}

netParams.connParams['STN->GPi'] = {
    'preConds': {'pop': 'STN_pop'}, 
    'postConds': {'pop': 'GPi_pop'},
    'weight': 0.111111,
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1,
    'synMech': 'AMPA',
    'delay': 2}

netParams.connParams['GPi->Th'] = {
    'preConds': {'pop': 'GPi_pop'}, 
    'postConds': {'pop': 'Th_pop'},
    'weight': 3,
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1,
    'synMech': 'GABA',
    'delay': 2}

netParams.connParams['GPe->GPi'] = {
    'preConds': {'pop': 'GPe_pop'}, 
    'postConds': {'pop': 'GPi_pop'},
    'weight': 0.111111,
    'convergence': 1,
    'sec': 'soma',
    'loc': 0.5,
    'synMech': 'GABA',
    'delay': 2}

netParams.connParams['GPe->STN'] = {
    'preConds': {'pop': 'GPe_pop'}, 
    'postConds': {'pop': 'STN_pop'},
    'weight': 0.111111,
    'convergence': 2,
    'sec': 'soma',
    'loc': 0.5,
    'synMech': 'GABA',
    'delay': 3}

#change weight for parkinsonian state
netParams.connParams['GPe->GPe'] = {
    'preConds': {'pop': 'GPe_pop'}, 
    'postConds': {'pop': 'GPe_pop'},
    'weight': 0.005, #0.015
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1,
    'synMech': 'GABA',
    'delay': 4}

#uncomment for parkinsonian state
# netParams.connParams['Str->GPe'] = {
#     'preConds': {'pop': 'Str_pop'}, 
#     'postConds': {'pop': 'GPe_pop'},
#     'weight': 0.01,
#     'convergence': 1,
#     'sec': 'soma',
#     'loc': 0.5,
#     'synMech': 'GABA',
#     'delay': 1}

netParams.connParams['Th->Cort'] = {
    'preConds': {'pop': 'Th_pop'}, 
    'postConds': {'pop': 'Cort_pop'},
    'weight': 5, 
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 1,
    'synMech': 'AMPA',
    'delay': 2}

### why do we need this population? 
# netParams.connParams['Cort->Th'] = {
#     'preConds': {'pop': 'Cort_pop'}, 
#     'postConds': {'pop': 'Th_pop'},
#     'weight': 0, 
#     'sec': 'soma',
#     'loc': 0.5,
#     'convergence': 1,
#     'synMech': 'AMPA',
#     'delay': 2}

netParams.connParams['Inter->Cortsoma'] = {
    'preConds': {'pop': 'Inter_pop'}, 
    'postConds': {'pop': 'Cort_pop'},
    'weight': 'uniform(0,6.0e-3)', 
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 10,
    'synMech': 'GABA',
    'delay': 2}

#should change the source in mechanism to axon!!! - did it
netParams.connParams['Cortaxon->Inter'] = {
    'preConds': {'pop': 'Cort_pop'}, 
    'postConds': {'pop': 'Inter_pop'},
    'weight': 'uniform(0,2.5e-3)', 
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 10,
    'synMech': 'AMPA_axon',
    'delay': 2}

netParams.connParams['Cortaxon->STN'] = {
    'preConds': {'pop': 'Cort_pop'}, 
    'postConds': {'pop': 'STN_pop'},
    'weight': 0.12, 
    'sec': 'soma',
    'loc': 0.5,
    'convergence': 5,
    'synMech': 'AMPA_axon',
    'delay': 1}

#%% cfg  
cfg = specs.SimConfig()					            # object of class SimConfig to store simulation configuration
cfg.duration = 1*1e3 						            # Duration of the simulation, in ms
cfg.dt = 0.01								                # Internal integration timestep to use
cfg.verbose = 0						                # Show detailed messages 
cfg.recordTraces = {'V_soma':{'sec':'soma','loc':0.5,'var':'v'}}  # Dict with traces to record
cfg.recordStep = 0.01 			
cfg.filename = 'model_output'  			# Set file output name
cfg.saveJson = False
cfg.analysis['plotTraces'] = {'include': [0,pop_Size,2*pop_Size, 3*pop_Size, 4*pop_Size, 5*pop_Size]} # Plot recorded traces for this list of cells
cfg.hParams['celsius'] = 36
cfg.hParams['v_init'] = -68

#%% run
sim.createSimulateAnalyze(netParams = netParams, simConfig = cfg)
sim.analysis.plot2Dnet(include = ['GPe_pop','STN_pop', 'GPi_pop', 'Th_pop', 'Inter_pop', 'Cort_pop']);
sim.analysis.plotSpikeStats();
#sim.analysis.plotShape(includePre=[], includePost=['Cort_pop'], showSyns=False, figSize=(4,9), dist=0.8, showFig=True)