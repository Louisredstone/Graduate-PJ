<?php
    if (isset($_POST['action']))
    {
        $tsk=$_POST['action'];
        switch($tsk){
            case "CPU":
                fclose(fopen("cache/LeNet_CPU.launch_training","w"));
            break;
            case "GPU":
                fclose(fopen("cache/LeNet_GPU.launch_training","w"));
            break;
            case "FPGA":
                fclose(fopen("cache/LeNet_FPGA.launch_training","w"));
            break;
        }
    }
?>