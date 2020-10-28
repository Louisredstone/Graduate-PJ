<?php
    if (isset($_POST['action']))
    {
        $tsk=$_POST['action'];
        switch($tsk){
            case "CPU":
                fclose(fopen("cache/LeNet_CPU.load","w"));
            break;
            case "GPU":
                fclose(fopen("cache/LeNet_GPU.load","w"));
            break;
            case "FPGA":
                fclose(fopen("cache/LeNet_FPGA.load","w"));
            break;
        }
    }
?>