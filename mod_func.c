#include <stdio.h>
#include "hocdec.h"
#define IMPORT extern __declspec(dllimport)
IMPORT int nrnmpi_myid, nrn_nobanner_;

extern void _Destexhe_Static_AMPA_Synapse_reg();
extern void _Destexhe_Static_GABAA_Synapse_reg();
extern void _Interneuron_I_K_reg();
extern void _Interneuron_I_Leak_reg();
extern void _Interneuron_I_Na_reg();
extern void _SynNoise_reg();
extern void _Thalamic_I_Na_K_reg();
extern void _Thalamic_I_T_reg();
extern void _Thalamic_I_leak_reg();
extern void _izhi2007b_reg();
extern void _myions_reg();
extern void _pGPeA_reg();
extern void _pSTN_reg();

void modl_reg(){
	//nrn_mswindll_stdio(stdin, stdout, stderr);
    if (!nrn_nobanner_) if (nrnmpi_myid < 1) {
	fprintf(stderr, "Additional mechanisms from files\n");

fprintf(stderr," Destexhe_Static_AMPA_Synapse.mod");
fprintf(stderr," Destexhe_Static_GABAA_Synapse.mod");
fprintf(stderr," Interneuron_I_K.mod");
fprintf(stderr," Interneuron_I_Leak.mod");
fprintf(stderr," Interneuron_I_Na.mod");
fprintf(stderr," SynNoise.mod");
fprintf(stderr," Thalamic_I_Na_K.mod");
fprintf(stderr," Thalamic_I_T.mod");
fprintf(stderr," Thalamic_I_leak.mod");
fprintf(stderr," izhi2007b.mod");
fprintf(stderr," myions.mod");
fprintf(stderr," pGPeA.mod");
fprintf(stderr," pSTN.mod");
fprintf(stderr, "\n");
    }
_Destexhe_Static_AMPA_Synapse_reg();
_Destexhe_Static_GABAA_Synapse_reg();
_Interneuron_I_K_reg();
_Interneuron_I_Leak_reg();
_Interneuron_I_Na_reg();
_SynNoise_reg();
_Thalamic_I_Na_K_reg();
_Thalamic_I_T_reg();
_Thalamic_I_leak_reg();
_izhi2007b_reg();
_myions_reg();
_pGPeA_reg();
_pSTN_reg();
}
