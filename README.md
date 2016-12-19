# YHDL
YHDL - HDL - Redefined

YHDL is a tool that adds loops to HDL.<br/>
<b>But, how are loops written?</b><br/>
Well, they can be written like this:<br/><br/>
<span style='font-family: Consolas'>
for(1..16) //rest of the code
</span><br/><br/>

For example, you may create a Mux16 like that (using regular Mux chips):
<pre>
CHIP Mux16
{
    IN a[16], b[16], sel;
    OUT out[16];
    
    PARTS:
    for(0..16) Mux(a=a[for], b=b[for], out=out[for]);
}
</pre>
<br/>
As you seen, you can use the word <u>for</u> inside a for loop, and it will be replaced by the current iteration number.<br/>
The previous example would iterate between 0 (inclusive) and 16 (exclusive).<br/>
You can also write mathematical expressions inside &lt;> in for loops. Example: &lt;for-1> will give you the iteration number minus one.<br/>

<h1>Using the yhdl -> hdl converter</h1>
You just save the dist folder somewhere (clone or download it), and add it to the environment variables.<br/>
Then, when you want to convert a yhdl to hdl file, just like you would use g++ or gcc, open the cmd in the directory of the file, type hdl <filename.yhdl> [dstfilename.hdl], and watch as magic happens.
<br/><br/>
<b>Enjoy!</b>