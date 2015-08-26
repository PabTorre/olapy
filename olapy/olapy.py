"""

Concepts

The OLAP cube is a data structure that allows us to quickly take different views of the data. it is optimized to reduce work on the DB.
Start Schema: The star schema separates business process data into facts, which hold the measurable, quantitative data about a business, and dimensions which are descriptive attributes related to fact data. Examples of fact data include sales price, sale quantity, and time, distance, speed, and weight measurements. Related dimension attribute examples include product models, product colors, product sizes, geographic locations, and salesperson names. [wikipedia:star_schema]
    Fact table: 
        records measurements or metrics for a specific event. 
        numeric values and FK's. 
    Dimension tables: 
        hold the descriptive information about the data. 
        
   SELECT 
   JOIN
   GROUP 
   FILTER
   AGGREGATE

"""


def build_fact_table(source_tables):
    """
    
    (dictionary)
    generates a fact table as a view in database. 
    
    inputs:
        sources: a dictionary where the keys are table names for tables in the 
        targe database, and the values are column names for the columns in that db. 
        
        The system will use any overlapping columns for JOINING the star. 
        
        
    Steps: 
        verify all table names against db. 
        verify all column names against db. 
        identify all overlapping columns. 
        verifty that all tables have overlapping columns. 
        Build query make all columns unique in the JOIN process. 
            
    
    """
    
    
    
def slice_cube(fact_table, dimensions, null_dim, sql_aggregates):
    """
    
    (str, list, list, list)
    Build a query that gets a slice of an olap cube from a fact table 
    inputs:
        fact_table: the base data for the cube. 
        dimensions: the dimensions that we can use for slicing and dicing. 
        null_dim: the dimensions that can have null values. 
        sql_aggregates: dimensions that are null for this slice. 
    
    """
    
    sql_dimensions = ''
    sql_groups =''
    for dim in dimensions:
        if dim not in null_dim:
            sql_dimensions += dim +','
            sql_groups += dim +','
        else: 
            sql_dimensions += 'null,'
    
    if sql_groups !='':
        sql_groups = 'GROUP BY '+sql_groups[:-1]    

    

    sql = str(
            """
            SELECT 
            
        -- dimensions. this list has to match the group_by list. 
                {0}
        -- values
                {1}
            
            FROM {2}
             {3}
            
    
            """.format(sql_dimensions, sql_aggregates, fact_table, sql_groups))
    return sql


def scramble_cube(fact_table,dimensions = []):
    """
    this function builds the sql_query to put together all sides of an olap cube. 
    inputs: 
        dimensions: name of the dimensions for the cube. 
        fact_table: name of the fact_Table for the cube
    fact_table='ft'
    dimensions = [0,1,2]
        slice_cube(ft, dimensions, null_dim=[0,1,2]) -- corner
        slice_cube(ft, dimensions, null_dim=[0,1]) -- edge
        slice_cube(ft, dimensions, null_dim=[0,2]) -- edge
        slice_cube(ft, dimensions, null_dim=[1,2]) -- edge
        slice_cube(ft, dimensions, null_dim=[0]) -- face
        slice_cube(ft, dimensions, null_dim=[1]) -- face 
        slice_cube(ft, dimensions, null_dim=[2]) -- face
        slice_cube(ft, dimensions, null_dim=[]) -- center
    """
    
    # corner
    sql=''
    
    for L in range(0, len(dimensions)+1):
      for subset in itertools.combinations(dimensions, L):
        null_dim= list(subset)
        sql+=slice_cube(fact_table, dimensions, null_dim) + " UNION "
    sql = sql[:-10]
    sql+=" ORDER BY {0}".format(str(dimensions).replace("[","").replace("]","").replace("'",""))
    
    return sql


