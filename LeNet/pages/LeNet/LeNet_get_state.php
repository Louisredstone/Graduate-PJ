<?php
    if (isset($_POST['action']))
    {
        $tsk=$_POST['action'];
        switch($tsk){
            case "CPU":
                if(file_exists("cache/LeNet_CPU.running")){
                    if(file_exists("cache/LeNet_CPU.training")){
                        echo "training";
                    }
                    else {
                        echo "idle";
                    }
                }
                else {
                    echo "closed";
                }
            break;
            case "GPU":
                if(file_exists("cache/LeNet_GPU.running")){
                    if(file_exists("cache/LeNet_GPU.training")){
                        echo "training";
                    }
                    else {
                        echo "idle";
                    }
                }
                else {
                    echo "closed";
                }
            break;
            case "FPGA":
                if(file_exists("cache/LeNet_FPGA.running")){
                    if(file_exists("cache/LeNet_FPGA.training")){
                        echo "training";
                    }
                    else {
                        echo "idle";
                    }
                }
                else {
                    echo "closed";
                }
            break;
        }
    }
?>