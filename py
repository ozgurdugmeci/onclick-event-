
 df_base= pd.DataFrame(report)
 df_base.columns=['Depo_No','Depo_Adı','Week','Tutar']
 #df_base= df_base.head(3)

 df_base['Kümüle_Tutar']= df_base.Tutar.cumsum() * -1
 x=df_base['Week'].values.tolist()
 y=df_base['Kümüle_Tutar'].values.tolist()
 #fig, ax= plt.subplots()
 #plt.plot(x,y,'g--',marker='o', color='b') 
 numbr_xx=str(numbr_xx)
 title= str(numbr_xx) + " Mağaza Envanter Fark Analizi, Sayım Haftası: " + str(saym)
 #fig.set_size_inches(10,4)
 #ax.set_title(title)
 #fig.suptitle(title, fontsize=16)
 df_base.plot(kind='line', x='Week', y='Kümüle_Tutar',color='blue',linestyle='--',marker='o',legend=None,figsize=(10,4))
 #plt.figure(figsize=(10,4))
 plt.xlabel('Hafta')
 plt.ylabel('Kümüle_Tutar')
 #ax.set_xlabel('Hafta')
 #ax.set_ylabel('Kümüle Tutar') 
 
 plt.title(numbr_xx + ' Mağaza Envanter Fark Analizi, Sayım Haftası: ' + saym)
 plt.gcf().canvas.mpl_connect('button_press_event', onclick)
 plt.show()
 
