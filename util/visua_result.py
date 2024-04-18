from sklearn import metrics
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt

def visualization(prob_result,real_labels):
    result_count = int(len(prob_result) / 5)
    prob_result1 = prob_result[0:result_count]
    prob_result2 = prob_result[result_count:2 * result_count]
    prob_result3 = prob_result[2 * result_count:3 * result_count]
    prob_result4 = prob_result[3 * result_count:4 * result_count]
    prob_result5 = prob_result[4 * result_count:5 * result_count]

    fpr1, tpr1, thresholds1 = roc_curve(real_labels, prob_result1)
    auc1 = metrics.auc(fpr1, tpr1)
    fpr2, tpr2, thresholds2 = roc_curve(real_labels, prob_result2)
    auc2 = metrics.auc(fpr2, tpr2)
    fpr3, tpr3, thresholds3 = roc_curve(real_labels, prob_result3)
    auc3 = metrics.auc(fpr3, tpr3)
    fpr4, tpr4, thresholds4 = roc_curve(real_labels, prob_result4)
    auc4 = metrics.auc(fpr4, tpr4)
    fpr5, tpr5, thresholds5 = roc_curve(real_labels, prob_result5)
    auc5 = metrics.auc(fpr5, tpr5)

    plt.rc('font', family='Times New Roman')
    plt.figure(dpi=600)
    plt.plot(fpr1, tpr1, 'salmon', label='First AUC = %0.02f' % auc1)
    plt.plot(fpr2, tpr2, 'paleturquoise', label='Second AUC = %0.02f' % auc2)
    plt.plot(fpr3, tpr3, 'violet', label='Third AUC = %0.02f' % auc3)
    plt.plot(fpr4, tpr4, 'palegreen', label='Forth AUC = %0.02f' % auc4)
    plt.plot(fpr5, tpr5, 'royalblue', label='Fifth AUC = %0.02f' % auc5)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.legend(loc='lower right')
    plt.xlabel('False Positive Rate', fontdict={'family': 'Times New Roman', 'size': 15})
    plt.ylabel('True Positive Rate', fontdict={'family': 'Times New Roman', 'size': 15})
    plt.title('AMP 5 Fold ROC', fontdict={'family': 'Times New Roman', 'size': 20})
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.show()




