<?php
    function getPicUrl($movieId) {
        $url = "http://www.imdb.com/title/".$movieId."/";
        //$url = "http://www.baidu.com";
        $page_content = file_get_contents($url) or die("no such url!!");
        preg_match("/<img src=\"(.+?)\".*?>/", $page_content, $res) or die("no such matching!!");
        echo $res[0]."aa";
        return $page_content;
    }
    
    
?>
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" type="text/css" href="css/base.css">
        <script type="text/javascript" src="js/base.js"></script>
    </head>
    <body onload="startLoad()">
        <div id="main">
            <div id="liked-movies">
                <ul id="liked-movies-list" class="drop-buckets">
                    <?php
                        $fileArr = array();
                        $file = fopen("../recommender/mark_liked_movie_id.txt", "r") or die("no such file!!");
                        while (!feof($file)) {
                            $id = fgets($file);
                            $fileArr[] = $id;
                        }
                        fclose($file);

                        foreach ($fileArr as $id) {
                            getPicUrl(trim($id));
                            echo "<li>$id</li>";
                        }
                    ?>

                </ul>
            </div>
            <div id="recommended-movies">
                <ul id="recommended-movies-list">
                    <?php
                        $recommendedMovies = exec("python ../recommender/recommender.py");
                        $recommendedMoviesId_tmp = explode(",", $recommendedMovies);
                        for ($i = 0; $i < count($recommendedMoviesId_tmp); $i++) {
                            $startPos = strpos($recommendedMoviesId_tmp[$i], "'") + 1;
                            $endPos = strrpos($recommendedMoviesId_tmp[$i], "'");
                            $len = $endPos - $startPos;
                            $recommendId = substr($recommendedMoviesId_tmp[$i], $startPos, $len);
                            

                            echo "<li>$recommendId</li>";
                        }
                    ?>
                </ul>
            </div>
        </div>
    </body>
</html>