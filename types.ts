export interface Transaction {
  date: string;
  description: string;
  amount: number;
  type: 'income' | 'expense';
  category: string;
}

export interface KPI {
  label: string;
  value: string;
  trend: number; // percentage change
  trendDirection: 'up' | 'down' | 'neutral';
}

export interface ChartDataPoint {
  name: string;
  income: number;
  expense: number;
  profit: number;
}

export interface CategoryDataPoint {
  name: string;
  value: number;
}

// New Interface for Theoretical Analysis (e.g., Pareto, Break-even)
export interface FinancialTheory {
  title: string;
  theoryDescription: string; // Educational description of the theory
  applicationAnalysis: string; // How it applies to this specific user data
  actionableStep: string; // What to do next based on this theory
  chartType: 'bar' | 'pie' | 'area';
  chartData: any[]; // Dynamic data for the specific theory chart
}

export interface Recommendation {
  title: string;
  description: string;
  impact: 'high' | 'medium' | 'low';
}

export interface AIAnalysisResult {
  summary: string;
  kpis: KPI[];
  monthlyData: ChartDataPoint[];
  expenseByCategory: CategoryDataPoint[];
  insights: string[];
  // Advanced Strategic Section
  advancedTheories: FinancialTheory[]; 
  strategicPlan: string;
  riskAssessment: string;
  recommendations: Recommendation[];
}

export enum AppView {
  LANDING = 'LANDING',
  INPUT = 'INPUT',
  DASHBOARD = 'DASHBOARD',
  REPORT = 'REPORT',
}