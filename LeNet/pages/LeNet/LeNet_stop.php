<?php
    if (isset($_POST['action']))
    {
        $tsk=$_POST['action'];
        switch($tsk){
            case "CPU":
                fclose(fopen("cache/LeNet_CPU.stopnow","w"));
            break;
            case "GPU":
                fclose(fopen("cache/LeNet_GPU.stopnow","w"));
            break;
            case "FPGA":
                fclose(fopen("cache/LeNet_FPGA.stopnow","w"));
            break;
        }
    }
?>