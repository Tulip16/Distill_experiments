python train_distill_learn_multilam_platt_scaling.py > platt_9.txt
echo "platt_9 done"
python train_distill_learn_multilam_all_train.py > all_train_9.txt
echo "all_train_9 done"
python temp_platt.py > platt_1.txt
echo "platt_1 done"
python temp_val.py > all_train_1.txt
echo "all_train_1 done"