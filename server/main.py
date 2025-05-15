import httpx
from mcp.server.fastmcp import FastMCP
import yfinance as yf

# Initialize FastMCP server
mcp = FastMCP("stock-api")

@mcp.tool()
async def get_stock_price(ticker: str) -> dict:
    """
    Get the current price of a stock.
    """
    try:
        # Fetch the stock price from Polygon API
        dat = yf.Ticker(ticker)
        response = dat.info
        if response:
            return {
                "ticker": ticker,
                "response": response,
            }
        else:
            return {"error": "Stock not found"}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
