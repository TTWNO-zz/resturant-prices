# Only lines that start with 'D' or 'C' without quotes are read
# D stands for dish, C stands for config
# Format:
# I:<cost>:<proper name>[:long arg name][:short arg name]
# short arg name defaults to first character
# long arg name defaults to prope name in lower case

D:3.80:small:--small:-s
D:4.95:medium:--medium:-m
D:5.80:large:--large:-l
D:6.80:extra large:--xlarge:-x
D:9.25:jumbo:--jumbo:-j
#Example:
#D:19.20:Chicken Parmasean:--chicken-parm:-chp

# C entries require type as second param
# float, int, and str are available
# Tax by precent
C:float:tax=5
