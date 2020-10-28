<?php
    if (isset($_POST['action']))
    {
        $tsk=$_POST['action'];
        switch($tsk){
            case "CPU":
                set_time_limit(1800);
                exec("LeNet_CPU_start.bat");
            break;
            case "GPU":
                set_time_limit(1800);
                exec("LeNet_GPU_start.bat");
            break;
            case "FPGA":
                set_time_limit(1800);
                exec("LeNet_FPGA_start.bat");
            break;
        }
    }
?>