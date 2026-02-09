#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مثال بسيط لاستخدام CostGuard AI
Simple example of using CostGuard AI
"""

import json
import pandas as pd

def read_analysis_results():
    """
    قراءة وعرض نتائج التحليل
    Read and display analysis results
    """
    print("=" * 70)
    print("📊 قراءة نتائج التحليل - Reading Analysis Results")
    print("=" * 70)
    
    # قراءة ملف JSON
    with open('../analysis_summary_ai.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # عرض المؤشرات الرئيسية
    print("\n📈 المؤشرات الرئيسية - Key Metrics:")
    print("-" * 70)
    summary = data['analysis_summary']
    print(f"إجمالي الإيرادات: {summary['total_revenue']:,.0f} ريال")
    print(f"صافي الربح: {summary['total_profit']:,.0f} ريال")
    print(f"هامش الربح: {summary['profit_margin']:.2f}%")
    print(f"عدد الطلبات: {summary['total_orders']:,}")
    
    # عرض نتائج AI
    if 'ai_insights' in data and data['ai_insights'].get('status') != 'ML_NOT_AVAILABLE':
        print("\n🤖 نتائج الذكاء الاصطناعي - AI Insights:")
        print("-" * 70)
        
        ai = data['ai_insights']
        
        # التنبؤ بالمبيعات
        if 'forecasting' in ai and ai['forecasting']['status'] == 'success':
            forecast = ai['forecasting']
            print(f"\n📊 التنبؤ بالمبيعات:")
            print(f"  • المبيعات المتوقعة (30 يوم): {forecast['total_predicted']:,.0f} ريال")
            print(f"  • المتوسط اليومي المتوقع: {forecast['daily_average']:,.0f} ريال")
            print(f"  • دقة النموذج: {forecast['accuracy_r2']*100:.2f}%")
        
        # كشف الحالات الشاذة
        if 'anomalies' in ai and ai['anomalies']['status'] == 'success':
            anomalies = ai['anomalies']
            print(f"\n🔍 كشف الحالات الشاذة:")
            print(f"  • عدد الحالات: {anomalies['total_anomalies']}")
            print(f"  • النسبة المئوية: {anomalies['anomaly_percentage']:.2f}%")
            print(f"  • القيمة الإجمالية: {anomalies['anomaly_total_value']:,.0f} ريال")
        
        # تحسين الأسعار
        if 'price_optimization' in ai and ai['price_optimization']['status'] == 'success':
            prices = ai['price_optimization']
            print(f"\n💲 تحسين الأسعار:")
            print(f"  • عدد المنتجات المحللة: {prices['total_products']}")
            print(f"  • منتجات تحتاج تعديل: {prices['products_need_change']}")
        
        # تجميع العملاء
        if 'segmentation' in ai and ai['segmentation']['status'] == 'success':
            segments = ai['segmentation']
            print(f"\n👥 تجميع العملاء:")
            print(f"  • عدد المجموعات: {segments['n_clusters']}")
            for seg, count in segments['segment_distribution'].items():
                print(f"  • مجموعة {int(seg)+1}: {count} عميل")
        
        # تحسين المخزون
        if 'inventory_optimization' in ai and ai['inventory_optimization']['status'] == 'success':
            inventory = ai['inventory_optimization']
            print(f"\n📦 تحسين المخزون:")
            print(f"  • منتجات سريعة الحركة: {inventory['fast_moving_count']}")
            print(f"  • إجمالي المنتجات: {inventory['total_products']}")
    
    print("\n" + "=" * 70)
    print("✅ تم عرض جميع النتائج بنجاح!")
    print("=" * 70)


def read_sales_data():
    """
    قراءة وعرض عينة من بيانات المبيعات
    Read and display sample sales data
    """
    print("\n" + "=" * 70)
    print("📋 عينة من بيانات المبيعات - Sales Data Sample")
    print("=" * 70)
    
    # قراءة CSV
    df = pd.read_csv('../salla_data_full.csv')
    
    print(f"\nإجمالي السجلات: {len(df):,}")
    print(f"الفترة: {df['التاريخ_والوقت'].min()} إلى {df['التاريخ_والوقت'].max()}")
    
    print("\nأول 5 طلبات:")
    print(df[['رقم_الطلب', 'المنتج', 'الفئة', 'إجمالي_المبيعات', 'صافي_الربح']].head())
    
    print("\nأعلى 5 منتجات مبيعاً:")
    top_products = df.groupby('المنتج')['إجمالي_المبيعات'].sum().sort_values(ascending=False).head()
    for product, sales in top_products.items():
        print(f"  • {product}: {sales:,.0f} ريال")


def main():
    """
    الدالة الرئيسية
    Main function
    """
    print("\n" + "=" * 70)
    print("🚀 CostGuard AI - مثال على الاستخدام")
    print("=" * 70)
    
    try:
        # قراءة النتائج
        read_analysis_results()
        
        # قراءة البيانات
        read_sales_data()
        
        print("\n✅ اكتمل المثال بنجاح!")
        
    except FileNotFoundError:
        print("\n❌ خطأ: الملفات المطلوبة غير موجودة!")
        print("   تأكد من تشغيل Financial.py أولاً لتوليد البيانات.")
    except Exception as e:
        print(f"\n❌ خطأ: {e}")


if __name__ == "__main__":
    main()
