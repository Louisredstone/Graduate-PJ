<?php
    if (isset($_POST['action']))
    {
        $tsk=$_POST['action'];
        switch($tsk){
            // case "LeNet_CPU_start":
            //     set_time_limit(1800);
            //     exec("LeNet_CPU_start.bat");
            // break;
            case "LeNet_CPU_stop":
                fclose(fopen("cache/LeNet_CPU.stopnow","w"));
            break;
            case "LeNet_CPU_load":
                fclose(fopen("cache/LeNet_CPU.load","w"));
            break;
            case "LeNet_CPU_save":
                fclose(fopen("cache/LeNet_CPU.save","w"));
            break;
            case "LeNet_CPU_launch_training":
                fclose(fopen("cache/LeNet_CPU.launch_training","w"));
            break;
            case "get_LeNet_CPU_log":
                $log=fopen("LeNet_CPU.log","r") or die("Unable to open file!");
                if (filesize("LeNet_CPU.log")>0){
                    $arr=array();
                    while(!feof($log)){
                        array_push($arr,fgets($log));
                    }
                    $init=0;
                    $ceil=8;
                    $content="";
                    if (count($arr)>$ceil){
                        $init=count($arr)-$ceil;
                    }
                    for($i=$init;$i<count($arr);$i++){
                        $encode = mb_detect_encoding($arr[$i], array("ASCII",'UTF-8',"GB2312","GBK",'BIG5')); 
                        $encoded_line= mb_convert_encoding($arr[$i], 'UTF-8', $encode);
                        $content="{$content}{$encoded_line}<br>";
                    }
                    // $content=fread($log,filesize("LeNet_CPU.log"));
                    // echo str_replace("\n","<br>",$content);
                    echo $content;
                }
                fclose($log);
            break;
            case "check_LeNet_CPU_running":
                if(file_exists("cache/LeNet_CPU.running")){
                    if(file_exists("cache/LeNet_CPU.training")){
                        echo 2;
                    }
                    else {
                        echo 1;
                    }
                }
                else {
                    echo 0;
                }
            break;
        }
    }
?>