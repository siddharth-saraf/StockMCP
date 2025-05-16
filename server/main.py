from mcp.server.fastmcp import FastMCP
import yfinance as yf

# Initialize FastMCP server
mcp = FastMCP("stock-api")

@mcp.tool()
async def get_stock_info(ticker: str) -> dict:
    """
    Get the information of a stock using its ticker symbol.
    Args:
        ticker (str): The stock ticker symbol.
    Returns:
        dict: A dictionary containing the following stock information:
            - symbol: Stock ticker symbol
            - shortName: Company's short name 
            - currentPrice: Current stock price
            - regularMarketChange: Price change from previous close
            - regularMarketChangePercent: Percentage change from previous close
            - regularMarketDayRange: Today's price range (low-high)
            - volume: Today's trading volume
            - marketCap: Company's market capitalization
            - fiftyTwoWeekRange: 52-week price range (low-high)
            - trailingPE: Price-to-earnings ratio (trailing 12 months)
            - dividendYield: Dividend yield as a percentage
            - sector: Company's sector
            - industry: Company's industry
            - recommendationKey: Analyst recommendations
    """
    try:
        # Fetch the stock price from yahoo finance
        dat = yf.Ticker(ticker)
        response = dat.info

        if response:
            # Extract only the important fields
            important_fields = [
                'symbol', 
                'shortName', 
                'currentPrice',
                'regularMarketChange',
                'regularMarketChangePercent',
                'regularMarketDayRange',
                'volume',
                'marketCap',
                'fiftyTwoWeekRange',
                'trailingPE',
                'dividendYield',
                'sector',
                'industry',
                'recommendationKey'
            ]
            
            # Create a filtered response with only the important fields
            filtered_data = {field: response.get(field) for field in important_fields if field in response}
            
            return {
                "ticker": ticker,
                "data": filtered_data
            }
        else:
            return {"error": "Stock not found"}
    
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
