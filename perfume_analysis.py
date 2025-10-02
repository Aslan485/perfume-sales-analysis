import pandas as pd
import numpy as np

def load_data(file_path):
    """Load dataset from CSV file"""
    return pd.read_csv(file_path)

def calculate_business_metrics(df):
    """Calculate key business performance metrics"""
    total_products = len(df)
    total_brands = df['brand'].nunique()
    total_sold = df['sold'].sum()
    avg_price = df['price'].mean()
    total_revenue = (df['price'] * df['sold']).sum()
    
    return {
        'total_products': total_products,
        'total_brands': total_brands,
        'total_sold': total_sold,
        'avg_price': avg_price,
        'total_revenue': total_revenue
    }

def analyze_top_brands(df, n=10):
    """Analyze top performing brands by sales volume"""
    brand_stats = df.groupby('brand').agg({
        'price': ['count', 'mean'],
        'sold': 'sum',
        'available': 'sum'
    }).round(2)
    
    brand_stats.columns = ['product_count', 'avg_price', 'total_sold', 'stock_quantity']
    brand_stats['sales_efficiency'] = (
        brand_stats['total_sold'] / 
        (brand_stats['total_sold'] + brand_stats['stock_quantity'])
    ).round(3)
    
    return brand_stats.nlargest(n, 'total_sold')

def analyze_price_segments(df):
    """Analyze sales performance by price segments"""
    def get_price_segment(price):
        if price <= 20: return 'Budget (≤$20)'
        elif price <= 50: return 'Mid-Range ($21-50)'
        elif price <= 100: return 'Premium ($51-100)'
        else: return 'Luxury (>$100)'
    
    df['price_segment'] = df['price'].apply(get_price_segment)
    
    segment_analysis = df.groupby('price_segment').agg({
        'brand': 'count',
        'price': 'mean',
        'sold': 'sum',
        'available': 'sum'
    }).round(2)
    
    segment_analysis['sales_ratio'] = (
        segment_analysis['sold'] / 
        (segment_analysis['sold'] + segment_analysis['available'])
    ).round(3)
    
    return segment_analysis

def analyze_product_types(df):
    """Analyze performance by product categories"""
    type_analysis = df.groupby('type').agg({
        'brand': 'count',
        'price': 'mean',
        'sold': 'sum'
    }).round(2).sort_values('sold', ascending=False)
    
    total_sold = df['sold'].sum()
    type_analysis['market_share'] = (type_analysis['sold'] / total_sold * 100).round(2)
    
    return type_analysis.head(10)

def get_best_selling_products(df, n=10):
    """Get top n best selling products"""
    return df.nlargest(n, 'sold')[['brand', 'title', 'type', 'price', 'sold']]

def analyze_inventory_efficiency(df):
    """Analyze inventory turnover and efficiency"""
    df['inventory_efficiency'] = (df['sold'] / (df['sold'] + df['available'])).round(3)
    
    most_efficient = df.nlargest(5, 'inventory_efficiency')[
        ['brand', 'title', 'price', 'sold', 'available', 'inventory_efficiency']
    ]
    least_efficient = df.nsmallest(5, 'inventory_efficiency')[
        ['brand', 'title', 'price', 'sold', 'available', 'inventory_efficiency']
    ]
    
    return most_efficient, least_efficient

def main():
    # Load data
    df = load_data(r"C:\Users\axund\Downloads\ebay_mens_perfume.csv")
    
    print("🛍️ E-commerce Perfume Sales Analysis")
    print("=" * 50)
    
    # 1. Key Metrics
    metrics = calculate_business_metrics(df)
    print("\n📊 KEY PERFORMANCE METRICS")
    print(f"Total Products: {metrics['total_products']}")
    print(f"Total Brands: {metrics['total_brands']}")
    print(f"Total Units Sold: {metrics['total_sold']:,}")
    print(f"Average Price: ${metrics['avg_price']:.2f}")
    print(f"Estimated Revenue: ${metrics['total_revenue']:,.2f}")
    
    # 2. Brand Analysis
    print("\n🏆 TOP 10 BRANDS BY SALES")
    top_brands = analyze_top_brands(df)
    print(top_brands)
    
    # 3. Price Segments
    print("\n💰 PRICE SEGMENT PERFORMANCE")
    segments = analyze_price_segments(df)
    print(segments)
    
    # 4. Product Types
    print("\n🧴 PRODUCT CATEGORY ANALYSIS")
    product_types = analyze_product_types(df)
    print(product_types)
    
    # 5. Best Sellers
    print("\n🔥 TOP 10 BEST SELLING PRODUCTS")
    best_sellers = get_best_selling_products(df)
    print(best_sellers.to_string(index=False))
    
    # 6. Inventory Efficiency
    print("\n📦 INVENTORY EFFICIENCY ANALYSIS")
    most_eff, least_eff = analyze_inventory_efficiency(df)
    print("Most Efficient Products:")
    print(most_eff.to_string(index=False))
    print("\nLeast Efficient Products:")
    print(least_eff.to_string(index=False))

if __name__ == "__main__":
    main()