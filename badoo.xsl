<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
<html>
<body>
<table border="1">
	<tr bgcolor="#CCCCCC">
		<td align="center"><strong>img</strong></td>
		<td align="center"><strong>age</strong></td>
		<td align="center"><strong>км</strong></td>
		<td align="center"><strong>url</strong></td>
	</tr>
	<xsl:for-each select="table/girl">
		<tr bgcolor="#F5F5F5">
			<td> <img> <xsl:attribute name="src">  <xsl:value-of select="@img"/> </xsl:attribute>  </img> </td> 
			<td> <xsl:value-of select="@age"/></td>
			<td> <xsl:value-of select="@location"/></td>
			<td><a> <xsl:attribute name="href">  <xsl:value-of select="@url"/></xsl:attribute> <xsl:value-of select="@name"/></a></td>
		</tr>
	</xsl:for-each>
</table>
</body>
</html>
</xsl:template>
</xsl:stylesheet>