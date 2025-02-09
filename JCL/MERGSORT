//MERGSORT JOB 1,NOTIFY=&SYSUID                                         00010000
//SORT     EXEC PGM=SORT                                                00020000
//SYSOUT   DD SYSOUT=*                                                  00030000
//SORTIN   DD DSN=&SYSUID..SOURCE(ROCKS1),DISP=SHR                      00040002
//         DD DSN=&SYSUID..SOURCE(ROCKS2),DISP=SHR                      00050002
//         DD DSN=&SYSUID..SOURCE(ROCKS3),DISP=SHR                      00060002
//SORTOUT  DD DSN=&SYSUID..OUTPUT(ROCKSOUT),DISP=(SHR)                  00070003
//SYSIN    DD *                                                         00090000
  SORT FIELDS=(1,20,CH,A)                                               00100001
/*                                                                      00110003
