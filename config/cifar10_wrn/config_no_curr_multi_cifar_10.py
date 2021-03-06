# LearninNet110', setting
config = dict(setting="supervisedlearning",

              dataset=dict(name="cifar10",
                           datadir="../data",
                           feature="dss",
                           type="pre-defined"),

              dataloader=dict(shuffle=True,
                              trn_batch_size=128,
                              val_batch_size=1000,
                              tst_batch_size=1000,
                              pin_memory=True),

              model=dict(architecture='WRN_16_X', 
                         numclasses=10,
                         teacher_arch=['WRN_16_X','WRN_16_X','WRN_16_X','WRN_16_X','WRN_16_X'], 
                         depth_teach = [16,16,16,16,16],
                         width_teach = [8,8,8,8,8],
                         depth = 16,
                         width = 1,
                         teacher_path=['results/No-curr_distil/cifar10/WRN_16_X_16_8_p0/16/model_40.pt',\
                         'results/No-curr_distil/cifar10/WRN_16_X_16_8_p0/16/model_80.pt',\
                         'results/No-curr_distil/cifar10/WRN_16_X_16_8_p0/16/model_120.pt',\
                         'results/No-curr_distil/cifar10/WRN_16_X_16_8_p0/16/model_160.pt',\
                         'results/No-curr_distil/cifar10/WRN_16_X_16_8_p0/16/model.pt']),
              
              ckpt=dict(is_load=False,
                        is_save=True,
                        is_save_pic=False,
                        dir='results/',
                        save_every=10),

              loss=dict(type='CrossEntropyLoss',
                        use_sigmoid=False),

              optimizer=dict(type="sgd",
                             momentum=0.9,
                             lr=0.1,
                             weight_decay=5e-4),

              scheduler=dict(type="Mstep",
                             T_max=200),

              ds_strategy=dict(type="No-curr",
                               warm_epoch=10,
                               decay=0.2,
                               schedule=[0, 10, 20, 40, 60, 100, 140, 170, 201],
                               sch_ind=1),

              train_args=dict(num_epochs=200,
                              device="cuda",
                              print_every=5,
                              results_dir='results/',
                              print_args=["val_loss", "val_acc", "tst_loss", "tst_acc", "time", "trn_loss", "trn_acc"],
                              return_args=[]
                              )
              )


