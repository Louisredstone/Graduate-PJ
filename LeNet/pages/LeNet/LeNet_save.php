<?php
    if (isset($_POST['action']))
    {
        $tsk=$_POST['action'];
        switch($tsk){
            case "CPU":
                fclose(fopen("cache/LeNet_CPU.save","w"));
            break;
            case "GPU":
                fclose(fopen("cache/LeNet_GPU.save","w"));
            break;
            case "FPGA":
                fclose(fopen("cache/LeNet_FPGA.save","w"));
            break;
        }
    }
?>