#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مثال متقدم: استخدام ميزات AI بشكل مستقل
Advanced example: Using AI features independently
"""

import sys
sys.path.append('..')

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# استيراد الدوال من الملف الرئيسي
try:
    from Financial import (
        ai_sales_forecasting,
        ai_customer_segmentation,
        ai_anomaly_detection,
        ai_price_optimization,
        ai_product_recommendations,
        ai_inventory_optimization
    )
except ImportError:
    print("❌ خطأ: لم يتم العثور على ملف Financial.py")
    print("   تأكد من تشغيل هذا السكريبت من مجلد examples/")
    sys.exit(1)


def example_load_your_data():
    """
    مثال على تحميل بياناتك الخاصة
    Example of loading your own data
    """
    print("\n" + "=" * 70)
    print("📂 مثال: تحميل بيانات مخصصة")
    print("=" * 70)
    
    # تحميل البيانات المولدة كمثال
    df = pd.read_csv('../salla_data_full.csv')
    
    # تحويل التاريخ إلى datetime
    df['التاريخ'] = pd.to_datetime(df['التاريخ_والوقت'])
    
    print(f"\n✅ تم تحميل {len(df):,} سجل")
    print(f"📅 الفترة: {df['التاريخ'].min().date()} إلى {df['التاريخ'].max().date()}")
    print(f"💰 إجمالي المبيعات: {df['إجمالي_المبيعات'].sum():,.0f} ريال")
    
    return df


def example_forecasting(df):
    """
    مثال على استخدام التنبؤ بالمبيعات
    Example of using sales forecasting
    """
    print("\n" + "=" * 70)
    print("🔮 مثال: التنبؤ بالمبيعات")
    print("=" * 70)
    
    result = ai_sales_forecasting(df)
    
    if result['status'] == 'success':
        print(f"\n✅ نجح التنبؤ!")
        print(f"📊 المبيعات المتوقعة للشهر القادم: {result['total_predicted']:,.0f} ريال")
        print(f"📈 المتوسط اليومي المتوقع: {result['daily_average']:,.0f} ريال")
        print(f"🎯 دقة النموذج (R²): {result['accuracy_r2']*100:.2f}%")
        print(f"📉 متوسط الخطأ: {result['mae']:,.0f} ريال")
        
        # يمكنك استخدام التنبؤات
        predictions = result['predictions']
        print(f"\n📅 التنبؤات لأول 7 أيام:")
        for i, pred in enumerate(predictions[:7], 1):
            print(f"  يوم {i}: {pred:,.0f} ريال")
    else:
        print(f"❌ فشل التنبؤ: {result.get('message', 'unknown error')}")


def example_customer_segmentation(df):
    """
    مثال على تجميع العملاء
    Example of customer segmentation
    """
    print("\n" + "=" * 70)
    print("👥 مثال: تجميع العملاء")
    print("=" * 70)
    
    result = ai_customer_segmentation(df)
    
    if result['status'] == 'success':
        print(f"\n✅ نجح التجميع!")
        print(f"📊 تم إنشاء {result['n_clusters']} مجموعة")
        
        # عرض المجموعات
        segments = result['segments']
        print(f"\n📋 تفاصيل المجموعات:")
        for seg in segments:
            print(f"\n  🏙️ {seg['المدينة']}:")
            print(f"     • المجموعة: {seg['اسم_المجموعة']}")
            print(f"     • القيمة المالية: {seg['القيمة_المالية']:,.0f} ريال")
            print(f"     • عدد الطلبات: {seg['التكرار']}")
    else:
        print(f"❌ فشل التجميع: {result.get('message', 'unknown error')}")


def example_anomaly_detection(df):
    """
    مثال على كشف الحالات الشاذة
    Example of anomaly detection
    """
    print("\n" + "=" * 70)
    print("🔍 مثال: كشف الحالات الشاذة")
    print("=" * 70)
    
    result = ai_anomaly_detection(df)
    
    if result['status'] == 'success':
        print(f"\n✅ نجح الكشف!")
        print(f"⚠️  تم اكتشاف {result['total_anomalies']} حالة شاذة")
        print(f"📊 النسبة: {result['anomaly_percentage']:.2f}% من إجمالي المعاملات")
        print(f"💰 القيمة الإجمالية: {result['anomaly_total_value']:,.0f} ريال")
        
        # عرض أعلى الحالات الشاذة
        if result['top_anomalies']:
            print(f"\n🔝 أعلى 5 حالات شاذة:")
            for i, anomaly in enumerate(result['top_anomalies'], 1):
                print(f"\n  {i}. {anomaly['رقم_الطلب']}:")
                print(f"     • المنتج: {anomaly['المنتج']}")
                print(f"     • القيمة: {anomaly['إجمالي_المبيعات']:,.0f} ريال")
                print(f"     • الربح: {anomaly['الربح']:,.0f} ريال")
    else:
        print(f"❌ فشل الكشف: {result.get('message', 'unknown error')}")


def example_price_optimization(df):
    """
    مثال على تحسين الأسعار
    Example of price optimization
    """
    print("\n" + "=" * 70)
    print("💲 مثال: تحسين الأسعار")
    print("=" * 70)
    
    result = ai_price_optimization(df)
    
    if result['status'] == 'success':
        print(f"\n✅ نجح التحليل!")
        print(f"📊 تم تحليل {result['total_products']} منتج")
        print(f"💡 {result['products_need_change']} منتج يحتاج تعديل سعر")
        
        # عرض التوصيات
        print(f"\n📋 عينة من التوصيات:")
        for i, suggestion in enumerate(result['suggestions'][:5], 1):
            print(f"\n  {i}. {suggestion['المنتج']}:")
            print(f"     • السعر الحالي: {suggestion['السعر_الحالي']:,.0f} ريال")
            print(f"     • الإجراء المقترح: {suggestion['الإجراء']}")
            if suggestion['الإجراء'] != 'الاحتفاظ بالسعر':
                print(f"     • السعر المقترح: {suggestion['السعر_المقترح']:,.0f} ريال")
                print(f"     • السبب: {suggestion['السبب']}")
    else:
        print(f"❌ فشل التحليل: {result.get('message', 'unknown error')}")


def example_inventory_optimization(df):
    """
    مثال على تحسين المخزون
    Example of inventory optimization
    """
    print("\n" + "=" * 70)
    print("📦 مثال: تحسين المخزون")
    print("=" * 70)
    
    # نحتاج لتمرير analysis أيضاً، لكن يمكننا استخدام dict فارغ كمثال
    result = ai_inventory_optimization(df, {})
    
    if result['status'] == 'success':
        print(f"\n✅ نجح التحليل!")
        print(f"📊 تم تحليل {result['total_products']} منتج")
        print(f"🚀 {result['fast_moving_count']} منتج سريع الحركة")
        
        # عرض أفضل المنتجات
        print(f"\n🏆 أعلى 5 منتجات من حيث سرعة الحركة:")
        for i, item in enumerate(result['inventory_suggestions'][:5], 1):
            print(f"\n  {i}. {item['المنتج']}:")
            print(f"     • معدل البيع اليومي: {item['معدل_البيع_اليومي']:.1f} قطعة")
            print(f"     • الكمية المثلى للمخزون: {item['الكمية_المثلى_للمخزون']} قطعة")
            print(f"     • نقطة إعادة الطلب: {item['نقطة_إعادة_الطلب']} قطعة")
            print(f"     • التصنيف: {item['التصنيف']}")
    else:
        print(f"❌ فشل التحليل: {result.get('message', 'unknown error')}")


def main():
    """
    الدالة الرئيسية
    Main function
    """
    print("\n" + "=" * 70)
    print("🤖 CostGuard AI - أمثلة متقدمة")
    print("=" * 70)
    
    # تحميل البيانات
    df = example_load_your_data()
    
    # أمثلة على استخدام كل ميزة
    example_forecasting(df)
    example_customer_segmentation(df)
    example_anomaly_detection(df)
    example_price_optimization(df)
    example_inventory_optimization(df)
    
    print("\n" + "=" * 70)
    print("✅ اكتملت جميع الأمثلة بنجاح!")
    print("=" * 70)
    print("\n💡 نصيحة: يمكنك تعديل هذه الأمثلة لاستخدامها مع بياناتك الخاصة")


if __name__ == "__main__":
    main()
