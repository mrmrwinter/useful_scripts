set terminal png tiny size 1400,1400
set output "/home/mike/Desktop/scripts/snakes/plot_pairs/hiCversion1.linear/nucmer/nucmer.91.png"
set size 1,1
set grid
unset key
set border 15
set tics scale 0
set xlabel "PGA_scaffold_46__1_contigs__length_50000"
set ylabel "PGA_scaffold_15__3_contigs__length_8277944"
set format "%.0f"
set mouse format "%.0f"
set mouse mouseformat "[%.0f, %.0f]"
if(GPVAL_VERSION < 5) set mouse clipboardformat "[%.0f, %.0f]"
set xrange [1:50000]
set yrange [1:8277944]
set style line 1  lt 1 lw 3 pt 6 ps 1
set style line 2  lt 3 lw 3 pt 6 ps 1
set style line 3  lt 2 lw 3 pt 6 ps 1
plot \
 "/home/mike/Desktop/scripts/snakes/plot_pairs/hiCversion1.linear/nucmer/nucmer.91.fplot" title "FWD" w lp ls 1, \
 "/home/mike/Desktop/scripts/snakes/plot_pairs/hiCversion1.linear/nucmer/nucmer.91.rplot" title "REV" w lp ls 2
