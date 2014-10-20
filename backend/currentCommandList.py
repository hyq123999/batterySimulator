internalResistance=[ 0.0155,0.0154,0.0153,0.0156,0.0158,0.0160,0.0151,0.0150,0.0152,0.0155,0.0159,0.0152\
                    ,0.0150,0.0158,0.0154,0.0155,0.0152,0.0154,0.0159,0.0150,0.0157,0.0151,0.0150,0.0161\
                    ,0.0153,0.0157,0.0154,0.0150,0.0149,0.0153,0.0155,0.0158,0.0152,0.0157,0.0155,0.0155\
                    ,0.0154,0.0152,0.0150,0.0148,0.0150,0.0151,0.0155,0.0157,0.0152,0.0159,0.0161,0.0157\
                    ,0.0152,0.0155,0.0155,0.0155,0.0158,0.0159,0.0152,0.0154,0.0156,0.0159,0.0151,0.0153\
                    ,0.0159,0.0153,0.0156,0.0151,0.0154,0.0153,0.0157,0.0158,0.0150,0.0155,0.0155,0.0153\
                    ,0.0155,0.0153,0.0158,0.0152,0.0160,0.0150,0.0154,0.0158,0.0158,0.0153,0.0152,0.0159\
                    ,0.0155,0.0154,0.0158,0.0159,0.0158,0.0153,0.0155,0.0155,0.0155,0.0155,0.0152,0.0155]

                    
initialQuantity=[4640,4650,4680,4630,4648,4655,4666,4690,4646,4687,4632,4611\
                ,4650,4654,4644,4651,4680,4639,4659,4611,4620,4629,4639,4642\
                ,4643,4646,4650,4660,4670,4630,4660,4670,4650,4640,4630,4668\
                ,4645,4659,4644,4649,4641,4655,4653,4621,4633,4659,4652,4638\
                ,4677,4652,4657,4663,4666,4629,4649,4633,4644,4655,4666,4634\
                ,4628,4624,4632,4670,4656,4635,4639,4659,4639,4670,4680,4650\
                ,4637,4650,4660,4630,4680,4620,4670,4640,4667,4655,4636,4651\
                ,4637,4682,4684,4633,4644,4622,4629,4627,4639,4649,4636,4621] 
               
for i,b in enumerate(tm.bg):
    b.quantity = initialQuantity[i]
    b.intR=internalResistance[i]
tm.bg.generateSpiceModel()
tm.updateInfo()
tm.clock=0
tm.backup()